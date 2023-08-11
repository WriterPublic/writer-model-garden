import os
import logging
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


# Model input text
class ModelRequest(BaseModel):
    instances: List[Dict]
    max_new_tokens: int = 200
    temperature: float = 0.2


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
    outputs = model(prompts,
                    max_new_tokens = request.max_new_tokens,
                    temperature = request.temperature)
    predictions = [out[0] for out in outputs]
    return ModelResponse(predictions=predictions)


@app.post("/health", response_model=HealthStatus)
@app.get("/health", response_model=HealthStatus)
@app.get("/ready", response_model=HealthStatus)
@app.get("/", response_model=HealthStatus)
def health_check() -> HealthStatus:
    return HealthStatus(up=model is not None)
