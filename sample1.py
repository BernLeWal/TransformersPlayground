#!/bin/python
"""
Translation from an english sentence into german. The model runs locally
Sample based on the iX article: [Hugging Face - Zentrale für KI Modelle](https://www.heise.de/select/ix/2023/13/2302013542051756278)
"""
model_id = "translation_en_to_de"

from transformers import pipeline
from tools import shell

translator = pipeline(model_id)

shell = shell.SimpleShell("Translation from EN to DE")
shell.print("Sample (enter the text in the next line): ")
shell.print("This is an article about Hugging Face in a magazine.")

while True:
    text_en = shell.nextLine()
    text_de = translator(text_en)[0]["translation_text"]
    shell.print(text_de)
