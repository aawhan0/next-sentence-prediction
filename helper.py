# helper.py

from transformers import pipeline

def initialize_model():
    # Function to initialize and return a text generation model
    generator = pipeline('text-generation', model='gpt2')
    return generator
