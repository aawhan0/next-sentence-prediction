# app.py

from transformers import pipeline, set_seed
import streamlit as st

# Initialize the GPT-2 model for text generation
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

# Streamlit UI
st.title("Next Sentence Prediction using Generative AI")

# Input text box for the user
input_text = st.text_input("Enter your sentence here:")

# Display generated sentences if input text exists
if input_text:
    st.subheader("Generated Sentences:")
    outputs = generator(input_text, max_length=50, num_return_sequences=3)
    for i, output in enumerate(outputs):
        st.write(f"{i+1}. {output['generated_text']}")
