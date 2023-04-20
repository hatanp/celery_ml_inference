from .celery import app
from celery.signals import worker_ready
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = None
model = None

@worker_ready.connect()
def worker_ready(**kwargs):
    global tokenizer, model
    model_name = "TurkuNLP/gpt3-finnish-13B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")
    print("done loading the model")

@app.task
def generate(text_in,**kwargs):
    global tokenizer, model
    inputs = tokenizer(text_in, return_tensors="pt").to("cuda")
    gen_tokens = model.generate(**inputs,**kwargs)
    out = tokenizer.batch_decode(gen_tokens)
    return out
