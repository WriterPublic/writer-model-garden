import os
import logging
import subprocess
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM


# Model input text
class ModelRequest(BaseModel):
    instances: List[Dict]
    parameters: Dict = {}


# Model output text
class ModelResponse(BaseModel):
    predictions: List[Dict]


# Check service status
class HealthStatus(BaseModel):
    up: bool


# Create app
app = FastAPI()

# Download model
logger = logging.getLogger("writer-model-garden")
logger.setLevel(logging.INFO)
logger.info("Printing Disk space stats")
result = subprocess.run(['df', '-kh'], stdout=subprocess.PIPE)
logger.info(result)

hf_model = os.environ.get("MODEL_ID")
logger.info(f"Starting model download {hf_model}")
tokenizer = AutoTokenizer.from_pretrained(hf_model)
model = AutoModelForCausalLM.from_pretrained(hf_model)
logger.info("Model Downloaded")


@app.post("/generate", response_model=ModelResponse)
@app.post("/", response_model=ModelResponse)
def generate(request: ModelRequest) -> ModelResponse:
    text = [i["text"] for i in request.instances]
    max_new_tokens = request.parameters.get("max_new_tokens", 200)
    temperature = request.parameters.get("temperature", 0.8)
    # temperature has to be a positive float
    temperature = 0.001 if temperature < 0.001 else temperature
    top_k = request.parameters.get("top_k", 50)
    top_p = request.parameters.get("top_p", 0.95)
    do_sample = request.parameters.get("do_sample", True)

    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    outputs = model.generate(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'], max_new_tokens = max_new_tokens + 1, temperature = temperature, top_k = top_k, top_p = top_p, do_sample = do_sample)
    encoded_results = [out[0] for out in outputs]
    predictions = [{"generated_text": tokenizer.decode(e, skip_special_tokens=True)} for e in encoded_results]
    return ModelResponse(predictions=predictions)


@app.post("/health", response_model=HealthStatus)
@app.get("/health", response_model=HealthStatus)
@app.get("/ready", response_model=HealthStatus)
@app.get("/", response_model=HealthStatus)
def health_check() -> HealthStatus:
    return HealthStatus(up=model is not None)
