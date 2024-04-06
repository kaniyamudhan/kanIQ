import os
from dotenv import load_dotenv
import streamlit as st
import textwrap
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    st.error("Error: API key not found. Please make sure to set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    try:
        return response.text
    except ValueError as e:
        st.error("Error: Failed to generate response. Please try again with a different input.")
        return None

st.set_page_config(page_title="KanIQ 😉",page_icon="🤖")
st.header("KanIQ 😉")

input_text = st.text_input("Input:", key="input")

submit_button = st.button("submit")

if submit_button:
    response = get_gemini_response(input_text)
    if response is not None:
        st.subheader("The Response is")
        st.write(response)
