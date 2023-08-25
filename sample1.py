#!/bin/python
"""
Translation from an english sentence into german. The model runs locally
Sample based on the iX article: [Hugging Face - Zentrale für KI Modelle](https://www.heise.de/select/ix/2023/13/2302013542051756278)
"""

from transformers import pipeline

translator = pipeline("translation_en_to_de")

text_en = "This is an article about Hugging Face in a magazine."
text_de = translator(text_en)

print(text_de)