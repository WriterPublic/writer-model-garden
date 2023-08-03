# Base Image for PyTorch
FROM nvcr.io/nvidia/pytorch:23.06-py3 AS base

# Install Poetry for dependency management
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Copy source files
WORKDIR /app
COPY pyproject.toml .

# Lock dependencies
RUN $HOME/.local/bin/poetry install
RUN $HOME/.local/bin/poetry export --without-hashes -f requirements.txt >> requirements.txt

# Model Garden Deploy Image
FROM nvcr.io/nvidia/pytorch:23.06-py3 AS deploy

# Install requirements
WORKDIR /app
COPY --from=base /app/requirements.txt /app/
RUN python -m pip install --no-cache-dir -r requirements.txt

# Set environment variables
ARG HF_MODEL_ARG
ENV HF_MODEL=$HF_MODEL_ARG
ENV INFER_PORT=7080

# Copy source files
COPY server.py .
COPY main.py .

# Download and run the model
CMD [ "python", "main.py" ]
