import os

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

# Download model if not already downloaded
model = None

def download_model():
    global model
    hf_model = os.environ.get("HF_MODEL", "Writer/palmyra-small")
    model = pipeline(model = hf_model, task = "text-generation")


@app.post("/generate", response_model=ModelResponse)
@app.post("/", response_model=ModelResponse)
def generate(request: ModelRequest) -> ModelResponse:
    if not model:
        download_model()
    out = model(request.text)[0]["sequence"]
    return ModelResponse(out=out)


@app.post("/health", response_model=HealthStatus)
@app.get("/health", response_model=HealthStatus)
@app.get("/ready", response_model=HealthStatus)
@app.get("/", response_model=HealthStatus)
def health_check() -> HealthStatus:
    return HealthStatus(up=model is not None)


