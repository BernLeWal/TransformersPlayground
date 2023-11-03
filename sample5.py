#!/bin/python
"""
Sample shows how to use the CodeLLAMA-Model from META to generate sourcecode via code-completion,
based on the article in https://github.com/huggingface/blog/blob/main/codellama.md
An overview of all CodeLLAMA models, see https://huggingface.co/codellama
"""
model_id = "codellama/CodeLlama-7b-hf"

from transformers import AutoTokenizer
import transformers
import torch
from tools import shell

tokenizer = AutoTokenizer.from_pretrained(model_id)
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)

shell = shell.SimpleShell("Sourcecode-completion with CodeLLAMA-7B")
shell.print("Sample (enter the text in the next line): ")
shell.print("def fibonacci(")

while True:
    prompt = shell.nextLine()
    sequences = pipeline(
        prompt,
        do_sample=True,
        temperature=0.2,
        top_p=0.9,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=100,
    )
    for seq in sequences:
        shell.print(seq['generated_text'])