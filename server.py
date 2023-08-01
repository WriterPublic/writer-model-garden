import os
import logging

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


# Model input text
class ModelRequest(BaseModel):
    text: str


# Model output text
class ModelResponse(BaseModel):
    out: str


# Check service status
class HealthStatus(BaseModel):
    up: bool


# Create app
app = FastAPI()

# Download model
logging.info("Starting model download")
hf_model = os.environ.get("HF_MODEL", "Writer/palmyra-small")
model = pipeline(model = hf_model, task = "text-generation")
logging.info("Model Downloaded")


@app.post("/generate", response_model=ModelResponse)
@app.post("/", response_model=ModelResponse)
def generate(request: ModelRequest) -> ModelResponse:
    out = model(request.text)
    out_text = out[0].get("generated_text")
    return ModelResponse(out=out_text)


@app.post("/health", response_model=HealthStatus)
@app.get("/health", response_model=HealthStatus)
@app.get("/ready", response_model=HealthStatus)
@app.get("/", response_model=HealthStatus)
def health_check() -> HealthStatus:
    return HealthStatus(up=model is not None)
