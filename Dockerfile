# Base Image for PyTorch
FROM nvcr.io/nvidia/pytorch:23.06-py3 AS base

# Install Poetry for dependency management
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Copy source files
WORKDIR /app
COPY . .

# Lock dependencies
RUN $HOME/.local/bin/poetry install
RUN $HOME/.local/bin/poetry export --without-hashes -f requirements.txt >> requirements.txt

# Model Garden Deploy Image
FROM nvcr.io/nvidia/pytorch:23.06-py3 AS deploy

# Copy source files
WORKDIR /app
COPY server.py .
COPY main.py .

# Install requirements
COPY --from=base /app/requirements.txt /app/
RUN python -m pip install --no-cache-dir -r requirements.txt

# Download and run the model
CMD [ "python", "main.py" ]
