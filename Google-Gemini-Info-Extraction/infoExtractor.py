# Created by triloki at 27-12-2023

import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
import streamlit as st
load_dotenv()


# GOOGLE_API_KEY from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Load gemini-pro-vision llm model
model = genai.GenerativeModel('gemini-pro-vision')

# Func to get rsponse from gemini llm
def response(input,image,prompt):
    resp = model.generate_content([input,image[0],prompt])
    return resp.text

def image_to_bytes(uploaded_file):
    if uploaded_file is not None:
        # convert files into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# streamlit configuration
st.set_page_config(
    page_title='Multi-Language Information Extractor',
    page_icon="",
    layout='centered',
    initial_sidebar_state='collapsed'
)
st.header("Google Gemini Application")
input = st.text_input("Input Prompt:", key="input")
upload_file = st.file_uploader("Choose an image-", type=["jpg","jpeg","png"])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the document")

prompt = """
You are an expert in understanding documents. We will upload a document and 
you will have to give answer and question based on document
"""

if submit:
    image_data = image_to_bytes(upload_file)
    resp = response(prompt,image_data,input)
    st.subheader("Response is")
    st.write(resp)