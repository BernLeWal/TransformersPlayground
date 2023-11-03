#!/bin/python
"""
Translation from a german sentence into english.
Sample taken from https://huggingface.co/google/bert2bert_L-24_wmt_de_en
"""
model_id = "google/bert2bert_L-24_wmt_de_en"


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tools import shell

tokenizer = AutoTokenizer.from_pretrained(model_id, pad_token="<pad>", eos_token="</s>", bos_token="<s>")
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

shell = shell.SimpleShell("Translation from DE to EN")
shell.print("Sample (enter the text in the next line): ")
shell.print("Willst du einen Kaffee trinken gehen mit mir?")
# should output
# Want to drink a kaffee go with me? .

while True:
    sentence = shell.nextLine()

    input_ids = tokenizer(sentence, return_tensors="pt", add_special_tokens=False).input_ids
    output_ids = model.generate(input_ids)[0]
    shell.print(tokenizer.decode(output_ids, skip_special_tokens=True))
