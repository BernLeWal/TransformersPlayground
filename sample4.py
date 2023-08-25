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
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablecode-instruct-alpha-3b")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablecode-instruct-alpha-3b",
  trust_remote_code=True,
  torch_dtype="auto",
)
model.cuda()
inputs = tokenizer("###Instruction\nGenerate a python function to find number of CPU cores###Response\n", return_tensors="pt").to("cuda")
tokens = model.generate(
  **inputs,
  max_new_tokens=48,
  temperature=0.2,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
