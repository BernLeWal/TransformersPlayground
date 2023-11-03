# Hugging Face - Transformers-Playground

Playground with samples for using the transformers library from Hugging Face (huggingface.co).

Samples:
* text translation en-de: samples based on the iX article: [Hugging Face - Zentrale für KI Modelle](https://www.heise.de/select/ix/2023/13/2302013542051756278) and https://huggingface.co/google/bert2bert_L-24_wmt_de_en
* text translation de_en
* code generation

## Pre-Requisites

* On windows activate the developer-mode see [Enable your device for development](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development):
* Install required packages: ```pip install -r requirements.txt```

Hint: use a virtual environment (VENV) for python and libraries
```.venv\Scripts\activate```

## Models used

Some of the models are gated, f.e. StableCode - so you need to:
  1. request access to the model on https://huggingface.co
  2. create a new token https://huggingface.co/settings/tokens
  3. run in a shell: ```huggingface-cli login```
     and paste the token there.

## Installation

### PyTorch
Fetch PIP install command from PyTorch Website: https://pytorch.org/get-started/locally/
On 4.8.2023 for my RTX2080 it was:
```shell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Transformers
```shell
pip install transformers
```

Finally update requirements.txt
```shell
pip3 freeze > requirements.txt
```

## Running

Select one of the sampleXYZ.py of your choice and run them.

* [sample1.py](sample1.py): Translation from an english sentence into german.  
  Using pipeline("translation_en_to_de")
* [sample2.py](sample2.py): Translation from a german sentence into english.  
  Using google/bert2bert_L-24_wmt_de_en
* [sample3.py](sample3.py): Chat with a local natural-LLM Falcon-7B.  
  Using tiiuae/falcon-7b-instruct, also runs on the GPU.
* [sample4.py](sample4.py): use the StableCode-Model from StabilityAI to generate sourcecode.  
  Using stabilityai/stablecode-instruct-alpha-3b, runs on the GPU.


## Troubleshooting

### Upgrade transformers library

```
pip install transformers --upgrade
```

