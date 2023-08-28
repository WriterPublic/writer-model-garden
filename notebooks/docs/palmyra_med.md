---
license: apache-2.0
language:
- en
tags:
- medical
- palmyra
---

# Palmyra-med-20b

## Model description
**Palmyra-med-20b** is a 20 billion parameter Large Language Model that has been uptrained on 
**Palmyra-Large** with a specialized custom-curated medical dataset. 
The main objective of this model is to enhance performance in tasks related to medical dialogue
and question-answering.

- **Developed by:** [https://writer.com/](https://writer.com/);
- **Model type:** Causal decoder-only;
- **Language(s) (NLP):** English;
- **License:** Apache 2.0;
- **Finetuned from model:** [Palmyra-20B](https://huggingface.co/Writer/palmyra-large).

### Model Source

[Palmyra-Med: Instruction-Based Fine-Tuning of LLMs Enhancing Medical Domain Performance](https://dev.writer.com/docs/palmyra-med-instruction-based-fine-tuning-of-llms-enhancing-medical-domain-performance)


## Uses


### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful. 

## Bias, Risks, and Limitations

Palmyra-Med-20B is mostly trained on English data, and will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Palmyra-Med-20B to develop guardrails and to take appropriate precautions for any production use.


## Usage 
The model is compatible with the huggingface `AutoModelForCausalLM` and can be easily run on a single 40GB A100.

```py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Writer/palmyra-med-20b"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto"
    torch_dtype=torch.float16,
)

prompt = "Can you explain in simple terms how vaccines help our body fight diseases?"

input_text = (
    "A chat between a curious user and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's questions. "
    "USER: {prompt} "
    "ASSISTANT:"
)

model_inputs = tokenizer(input_text.format(prompt=prompt), return_tensors="pt").to(
    "cuda"
)

gen_conf = {
    "temperature": 0.7,
    "repetition_penalty": 1.0,
    "max_new_tokens": 512,
    "do_sample": True,
}

out_tokens = model.generate(**model_inputs, **gen_conf)

response_ids = out_tokens[0][len(model_inputs.input_ids[0]) :]
output = tokenizer.decode(response_ids, skip_special_tokens=True)

print(output)
## output ##
# Vaccines stimulate the production of antibodies by the body's immune system.
# Antibodies are proteins produced by B lymphocytes in response to foreign substances,such as viruses and bacteria.
# The antibodies produced by the immune system can bind to and neutralize the pathogens, preventing them from invading and damaging the host cells.
# Vaccines work by introducing antigens, which are components of the pathogen, into the body.
# The immune system then produces antibodies against the antigens, which can recognize and neutralize the pathogen if it enters the body in the future.
# The use of vaccines has led to a significant reduction in the incidence and severity of many diseases, including measles, mumps, rubella, and polio. 
```

It can also be used with text-generation-inference

```sh
model=Writer/palmyra-med-20b
volume=$PWD/data

docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference --model-id $model
```

##  Dataset
For the fine-tuning of our LLMs, we used a custom-curated medical dataset that combines data from
two publicly available sources: PubMedQA (Jin et al. 2019) and MedQA (Zhang et al. 2018).The
PubMedQA dataset, which originated from the PubMed abstract database, consists of biomedical
articles accompanied by corresponding question-answer pairs. In contrast, the MedQA dataset
features medical questions and answers that are designed to assess the reasoning capabilities of
medical question-answering systems.
We prepared our custom dataset by merging and processing data from the aforementioned sources,
maintaining the dataset mixture ratios detailed in Table 1. These ratios were consistent for finetuning
both Palmyra-20b and Palmyra-40b models. Upon fine-tuning the models with this dataset, we refer
to the resulting models as Palmyra-Med-20b and Palmyra-Med-40b, respectively.


| Dataset | Ratio    | Count |
| -----------|----------- | ----------- |
| PubMedQA | 75%       | 150,000       |
| MedQA | 25%    | 10,178        |


## Evaluation
we present the findings of our experiments, beginning with the evaluation outcomes of
the fine-tuned models and followed by a discussion of the base models’ performance on each of the
evaluation datasets. Additionally, we report the progressive improvement of the Palmyra-Med-40b
model throughout the training process on the PubMedQA dataset.

| Model | PubMedQA    | MedQA |
| -----------|----------- | ----------- |
| Palmyra-20b | 49.8       | 31.2       |
| Palmyra-40b | 64.8 | 43.1| 
| Palmyra-Med-20b|  75.6 | 44.6| 
| Palmyra-Med-40b|  81.1 | 72.4| 



## Limitation
The model may not operate efficiently beyond the confines of the healthcare field.
Since it has not been subjected to practical scenarios, its real-time efficacy and precision remain undetermined.
Under no circumstances should it replace the advice of a medical professional, and it must be regarded solely as a tool for research purposes.

## Citation and Related Information


To cite this model:
```
@misc{Palmyra-Med-20B,
  author = {Writer Engineering team},
  title = {{Palmyra-Large Parameter Autoregressive Language Model}},
  howpublished = {\url{https://dev.writer.com}},
  year = 2023,
  month = March 
}
```

## Contact
Hello@writer.com
