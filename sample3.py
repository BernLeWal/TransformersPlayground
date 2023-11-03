#!/bin/python
"""
Chat with a local natural-LLM Falcon-7B.
Sample based on the ct-Article Sprach-KI Falcon, see https://ct.de/y2t4
"""
model_id = "tiiuae/falcon-7b-instruct"

from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
from tools import shell

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
#model.config.pad_token_id = model.config.eos_token_id # suppress eos_token_id warning

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

shell = shell.SimpleShell("Chat with Falcon-7B")
shell.print("Sample (enter the text in the next line): ")
shell.print("What is the longest river in the world?")

while True:
    prompt = shell.nextLine()
    sequences = pipeline(
        prompt,
        max_length=200,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id
    )
    for seq in sequences:
        shell.print(seq['generated_text'])
