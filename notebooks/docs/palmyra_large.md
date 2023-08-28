---
language:
- en
datasets:
- English
- Writer/palmyra-data-index
tags:
- text generation
- pytorch
- causal-lm
- Writer-data
- gpt
- palmyra
pipeline_tag: text-generation
library_name: transformers
license: apache-2.0
---



# Palmyra Large 20B

**Palmyra-Large is a 20B parameters causal decoder-only model built by [Writer](https://www.Writer.com) and trained on +800B tokens of [Palmyra-Index-Data](https://huggingface.co/datasets/Writer/palmyra-data-index) enhanced with curated corpora.**



|[![Model architecture](https://img.shields.io/badge/Model%20Arch-Transformer%20Decoder-green)](#model-architecture)|[![Model size](https://img.shields.io/badge/Params-20B-green)](#model-architecture)|[![Language](https://img.shields.io/badge/Language-en--US-lightgrey#model-badge)](#datasets)


## Model Details

Palmyra Large was primarily pre-trained with English text. Note that there is still a trace amount of non-English data present within the training corpus that was accessed through CommonCrawl. A causal language modeling (CLM) objective was utilized during the process of the model's pretraining. Similar to GPT-3, Palmyra Large is a member of the same family of models that only contain a decoder. As a result, it was pre-trained utilizing the objective of self-supervised causal language modeling.

### Model Description

- **Developed by:** [https://www.writer.com](https://www.writer.com);
- **Model type:** Causal decoder-only;
- **Language(s) (NLP):** English (and limited capabilities in German, Spanish, French, Swedish);
- **License:** Apache 2.0 license.


## Uses

### Direct Use

Research on large language models; as a foundation for further specialization and finetuning for specific usecases (e.g., summarization, text generation, chatbot, etc.)

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful. 

## Bias, Risks, and Limitations

Palmyra-large-20B is trained mostly on English with limited capabilities also in German, Spanish, French, Swedish. It will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Palmyra-Large-20B to consider finetuning it for the specific set of tasks of interest, and for guardrails and appropriate precautions to be taken for any production use.


### Use case
Palmyra Large is extremely powerful while being extremely fast. This model excels at many nuanced tasks such as sentiment classification and summarization.


## Training data

Palmyra Large (20b) was trained on Writer’s custom dataset.


## Intended Use and Limitations

Palmyra Large learns an inner representation of the English language that can be used to extract features useful for downstream tasks. However, the model is best at what it was pre-trained for which is generating text from a prompt.

### How to use

This model can be easily loaded using the `AutoModelForCausalLM` functionality:

```python
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

# set HF environment variable
auth_token = os.environ.get("HF_TOKEN", True)

model = AutoModelForCausalLM.from_pretrained(
    "Writer/palmyra-large",
    device_map="auto",
    torch_dtype=torch.float16,
    use_auth_token=auth_token,
)

tokenizer = AutoTokenizer.from_pretrained(
    "Writer/palmyra-large", use_auth_token=auth_token
)

```

It can also be used with text-generation-inference

```sh
model=Writer/palmyra-large
volume=$PWD/data

docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference --model-id $model
```

### Limitations and Biases

Palmyra Large’s core functionality is to take a string of text and predict the next token. While language models are widely used for other tasks, there are many unknowns in this work. When prompting Palmyra Large, keep in mind that the next statistically likely token is not always the token that produces the most "accurate" text. Never rely on Palmyra Large to produce factually correct results.

Palmyra Large was trained on Writer’s custom data. As with all language models, it is difficult to predict how Palmyra Large will respond to specific prompts, and offensive content may appear unexpectedly. We recommend that the outputs be curated or filtered by humans before they are released, both to censor undesirable content and to improve the quality of the results.


## Citation and Related Information


To cite this model:
```
@misc{Palmyra,
  author = {Writer Engineering team},
  title = {{Palmyra-Large Parameter Autoregressive Language Model}},
  howpublished = {\url{https://dev.writer.com}},
  year = 2023,
  month = March 
}
```
## Contact
Hello@writer.com
