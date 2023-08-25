# Hugging Face - Transformers-Playground

Samples for using the transformers library from Hugging Face

Based on the iX article: [Hugging Face - Zentrale für KI Modelle](https://www.heise.de/select/ix/2023/13/2302013542051756278)

## Pre-Requisites

* On windows activate the developer-mode see [Enable your device for development](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development):
* Install required packages: ```pip install -r requirements.txt```

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