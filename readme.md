# Writer Model Garden

This repo contains the logic to deploy and run Writer's models on vertex AI. For each model, we have a separate notebook and a readme that explains the model.
The docker container needs the model name as an arg to download that model when the container runs.

The model notebooks upload each model to Model Registry and deploy it on an Endpoint. The notebook contains some example prediction requests to run against the endpoint and some of the parameters that can be passed to the model.

