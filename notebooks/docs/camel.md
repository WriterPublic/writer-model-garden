# Camel 🐪 5B

Instruction-following large language model suitable for generating contextually appropraite responses.

<style>
img {
 display: inline;
}
</style>


## Overview

Introducing Camel-5B, a state-of-the-art instruction-following large language model designed to deliver exceptional performance and versatility. Derived from the foundational architecture of [Palmyra-Base](https://huggingface.co/Writer/palmyra-base), Camel-5b is specifically tailored to address the growing demand for advanced natural language processing and comprehension capabilities.

The Camel-5b model is meticulously trained on an extensive dataset of approximately 70,000 instruction-response records. These records are generated by our dedicated Writer Linguist team, who possess considerable expertise in language modeling and fine-tuning techniques. By leveraging their skills and knowledge, the Camel-5B model is primed to offer unparalleled proficiency in understanding and executing language-based instructions.

One of the key differentiators of Camel-5b lies in its ability to process complex instructions and generate accurate, contextually appropriate responses. This makes it an ideal choice for a wide range of applications, including virtual assistants, customer support, content generation, and more. Additionally, the model's comprehensive training enables it to adapt and perform well under varying conditions and contexts, further expanding its potential use cases.


## Use Cases

Text Generation: Given a prompt with an instruction, the model will generate text to follow the instruction in the prompt.


## Documentation

This model can be used in a notebook. Click Open notebook to use the model in Colab.

Following the example in the notebook, Camel-5B will be uploaded to Model Registry and deployed to an endpoint in Vertex AI. After the deployment is successful, you can use vertex online predictions for text generation. The notebook shows an example of that.

It's easy to use the endpoint where we just deployed the model for online prediction anywhere. All you need is a reference to the endpoint, which you can get using one line of code:

```endpoint = aiplatform.Endpoint('projects/{PROJECT_UID}/locations/{REGION}/endpoints/{ENDPOINT_UID}')```

Remember to delete the model and the endpoint after you're done!


## Limitations and Biases

Camel's core functionality is to take a string of text and predict the next token. While language models are widely used for other tasks, there are many unknowns in this work. When prompting Camel, keep in mind that the next statistically likely token is not always the token that produces the most "accurate" text. Never rely on Camel to produce factually correct results.

Camel was trained on Writer’s custom data. As with all language models, it is difficult to predict how Camel will respond to specific prompts, and offensive content may appear unexpectedly. We recommend that the outputs be curated or filtered by humans before they are released, both to censor undesirable content and to improve the quality of the results.


## Camel VS. Llama

The Camel is essentially the Swiss Army knife of the animal kingdom - it can store water in its humps, survive extreme temperatures, and even provide a cushy ride for weary travelers. The llama, on the other hand, is basically just a glorified lawnmower with an attitude problem. Sure, they might have a cute, fuzzy face, but don't be deceived - one false move and you'll be greeted with a spit shower. The true MVP of the desert, and let the llama keep on spitting its way into obscurity.

<img src="https://i.postimg.cc/wjXZLQbB/Camel-Llama.png" width="400px" />