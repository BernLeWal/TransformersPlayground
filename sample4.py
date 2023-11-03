#!/bin/python
"""
Sample shows how to use the StableCode-Model from StabilityAI to generate sourcecode,
based on the sample in huggingface.co, see https://huggingface.co/stabilityai/stablecode-instruct-alpha-3b

Some more information see: https://www.unite.ai/what-to-know-about-stablecode-the-ai-code-generator-from-stability-ai/

ATTENTION: the model is gated, you need to
  1. request access to the model on https://huggingface.co
  2. create a new token https://huggingface.co/settings/tokens
  3. run in a shell: huggingface-cli login
     and paste the token there.
"""
model_id = "stabilityai/stablecode-instruct-alpha-3b"

from transformers import AutoModelForCausalLM, AutoTokenizer
from tools import shell

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
  model_id,
  trust_remote_code=True,
  torch_dtype="auto",
)
model.cuda()

shell = shell.SimpleShell("Generate source with StableCode-3B")
shell.print("Sample (enter the text in the next line): ")
shell.print("Generate a python function to find number of CPU cores")

while True:
  prompt = shell.nextLine()

  inputs = tokenizer(f"###Instruction\n{prompt}###Response\n", return_tensors="pt", return_token_type_ids=False).to("cuda")
  tokens = model.generate(
    **inputs,
    max_new_tokens=84,
    temperature=0.2,
    do_sample=True,
  )
  shell.print(tokenizer.decode(tokens[0], skip_special_tokens=True))
