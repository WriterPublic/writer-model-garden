# Palmyra Base 5B
Lightweight Causal Language Model (CLM) that excels at text generation, sentiment classification, and summarization.


## Overview

Palmyra Base was primarily pre-trained with English text. Note that there is still a trace amount of non-English data present within the training corpus that was accessed through CommonCrawl. A causal language modeling (CLM) objective was utilized during the process of the model's pretraining. Similar to GPT-3, Palmyra Base is a member of the same family of models that only contain a decoder. As a result, it was pre-trained utilizing the objective of self-supervised causal language modeling. Palmyra Base uses the prompts and general experimental setup from GPT-3 in order to conduct its evaluation per GPT-3.


## Use case
Palmyra Base is extremely powerful while being extremely fast. This model excels at many nuanced tasks such as sentiment classification and summarization.


## Documentation

This model can be used in a notebook. Click Open notebook to use the model in Colab.

Following the example in the notebook, Palmyra Base will be uploaded to Model Registry and deployed to an endpoint in Vertex AI. After the deployment is successful, you can use vertex online predictions for text generation. The notebook shows an example of that.

It's easy to use the endpoint where we just deployed the model for online prediction anywhere. All you need is a reference to the endpoint, which you can get using one line of code:

```endpoint = aiplatform.Endpoint('projects/{PROJECT_UID}/locations/{REGION}/endpoints/{ENDPOINT_UID}')```

Remember to delete the model and the endpoint after you're done!


## Training data

Palmyra Base (5B) was trained on Writer’s custom dataset.


## Intended Use and Limitations

Palmyra Base learns an inner representation of the English language that can be used to extract features useful for downstream tasks. However, the model is best at what it was pre-trained for which is generating text from a prompt.

### Limitations and Biases

Palmyra Base’s core functionality is to take a string of text and predict the next token. While language models are widely used for other tasks, there are many unknowns in this work. When prompting Palmyra Base, keep in mind that the next statistically likely token is not always the token that produces the most "accurate" text. Never rely on Palmyra Base to produce factually correct results.

Palmyra Base was trained on Writer’s custom data. As with all language models, it is difficult to predict how Palmyra Base will respond to specific prompts, and offensive content may appear unexpectedly. We recommend that the outputs be curated or filtered by humans before they are released, both to censor undesirable content and to improve the quality of the results.


## Evaluation results

Evaluation of Palmyra-base model on the SuperGLUE benchmark


|   Task     | Metric | Value |
|------------|--------|-------|
|   boolq    |  acc   | 64.43 |
|   cb       |  acc   | 10.71 |
|            |  f1    | 08.32 |
|   copa     |  acc   | 76.00 |
|   multirc  |  acc   | 01.26 |
|   record   |  f1    | 84.02 |
|            |  em    | 83.29 |
|   wic      |  acc   | 50.00 |
|   wsc      |  acc   | 36.54 |
