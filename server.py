import os
import logging
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


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
logging.info("Starting model download")
hf_model = os.environ.get("HF_MODEL", "Writer/palmyra-base")
model = pipeline(model = hf_model, task = "text-generation")
logging.info("Model Downloaded")


@app.post("/generate", response_model=ModelResponse)
@app.post("/", response_model=ModelResponse)
def generate(request: ModelRequest) -> ModelResponse:
    prompts = [i["text"] for i in request.instances]
    max_new_tokens = request.parameters.get("max_new_tokens", 200)
    temperature = request.parameters.get("temperature", 0.8)
    # temperature has to be a positive float
    temperature = 0.001 if temperature < 0.001 else temperature
    top_k = request.parameters.get("top_k", 50)
    top_p = request.parameters.get("top_p", 0.95)
    do_sample = request.parameters.get("do_sample", True)
    outputs = model(prompts,
                    max_new_tokens = max_new_tokens,
                    temperature = temperature,
                    top_k = top_k,
                    top_p = top_p,
                    do_sample = do_sample)
    predictions = [out[0] for out in outputs]
    return ModelResponse(predictions=predictions)


@app.post("/health", response_model=HealthStatus)
@app.get("/health", response_model=HealthStatus)
@app.get("/ready", response_model=HealthStatus)
@app.get("/", response_model=HealthStatus)
def health_check() -> HealthStatus:
    return HealthStatus(up=model is not None)
