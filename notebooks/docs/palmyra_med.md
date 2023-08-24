# Palmyra Med 20B
Large Language Model (LLM) trained on a custom medical dataset to enhance the performance in tasks related to medical dialogue.


## Overview
Palmyra-Med-20B is a 20 billion parameter Large Language Model that has been uptrained on Palmyra-Large with a specialized custom curated medical dataset. 
The main objective of this model is to enhance performance in tasks related to medical dialogue and question-answering.


## Use case
Palmyra Med is extremely powerful while being extremely fast. Because of its training dataset, it excels at tasks focused on medical text such as entity recognition, question answering, and summarization.


## Documentation

This model can be used in a notebook. Click Open notebook to use the model in Colab.

Following the example in the notebook, Camel-5B will be uploaded to Model Registry and deployed to an endpoint in Vertex AI. After the deployment is successful, you can use vertex online predictions for text generation. The notebook shows an example of that.

It's easy to use the endpoint where we just deployed the model for online prediction anywhere. All you need is a reference to the endpoint, which you can get using one line of code:

```endpoint = aiplatform.Endpoint('projects/{PROJECT_UID}/locations/{REGION}/endpoints/{ENDPOINT_UID}')```

Remember to delete the model and the endpoint after you're done!


## Limitation
The model may not operate efficiently beyond the confines of the healthcare field.
Since it has not been subjected to practical scenarios, its real-time efficacy and precision remain undetermined.
Under no circumstances should it replace the advice of a medical professional, and it must be regarded solely as a tool for research purposes.

