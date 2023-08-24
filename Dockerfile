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

# Install transformers from source.
RUN git clone --depth 1 --branch v4.31.0 https://github.com/huggingface/transformers.git
# The patch is used to change the transformers loading model behavior:
# 1) For models on Huggingface hub: if the model has multiple shards, each shard
#    will be downloaded separately and get deleted after loading to GPU.
# 2) For models on local disk: if a model bin file is actually a text file
#    recording a GCS path, the model file will be downloaded and get deleted
#    after loading to GPU.
COPY hf_transformers_lazy_download.patch .
WORKDIR /app/transformers
RUN git apply /app/hf_transformers_lazy_download.patch
RUN pip install -e .

# Set environment variables
ENV INFER_PORT=7080

# Copy source files
WORKDIR /app
COPY server.py .
COPY main.py .

# Download and run the model
CMD [ "python", "main.py" ]
