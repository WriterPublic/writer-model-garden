This repo contains the logic to deploy Writer's models on vertex. For each model, we create a separate docker image to use in that model's notebook.
The docker image needs the model name as an arg to download that model when the container runs.

These are example commands to build the docker images:

# To build the image for Camel:

`docker build --build-arg HF_MODEL_ARG=Writer/camel-5b-hf -t writer-model-garden:camel .`

# To build the image for Plamyra Base

`docker build --build-arg HF_MODEL_ARG=Writer/palmyra-base -t writer-model-garden:base .`

# To build the image for Palmyra Large

`docker build --build-arg HF_MODEL_ARG=Writer/palmyra-large -t writer-model-garden:large .`

# To build the image for Palmyra Med

`docker build --build-arg HF_MODEL_ARG=Writer/palmyra-med-20b -t writer-model-garden:med .`

