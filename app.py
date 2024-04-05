import os
from dotenv import load_dotenv
import streamlit as st
import textwrap
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure API key
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    st.error("Error: API key not found. Please make sure to set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# Function to load OpenAI model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    try:
        return response.text
    except ValueError as e:
        st.error("Error: Failed to generate response. Please try again with a different input.")
        return None

# Initialize Streamlit app
st.set_page_config(page_title="kaxz")
st.header("kaxz ask")

# Input box for the question
input_text = st.text_input("Input:", key="input")

# Button to submit the question
submit_button = st.button("submit")

# If the submit button is clicked
if submit_button:
    response = get_gemini_response(input_text)
    if response is not None:
        st.subheader("The Response is")
        st.write(response)
