#!\bin\python
from transformers import pipeline

translator = pipeline("translation_en_to_de")

text_en = "This is an article about Hugging Face in a magazine."
text_de = translator(text_en)

print(text_de)