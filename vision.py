from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
from PIL import Image
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    st.error("Error: API key not found. Please make sure to set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    try:
        return response.text
    except ValueError as e:
        st.error("Error: Failed to generate response. Please try again with a different input or try again later")
        return None

#Streamlit app
st.set_page_config(page_title="KanIQ 😉",page_icon="🤖")
# st.sidebar.title("Sidebar")

st.header("KanIQ 😉")
st.write("**Unlock the content within your images! Upload a photo and let KanIQ craft a creative narrative.**")  # Added description

# Input box
# ... (your existing code)

# Example
 # Replace with a placeholder image and set width


# Input box 
input_prompt = st.text_input("Input Prompt:", key="input")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image Uploaded Successfully ✅.", use_column_width=True)

# Button submit 
submit_button = st.button("Tell me about the image ")

# after clicked
if submit_button:
    if image is None:
        st.warning("Please upload an image 👆🏻.")
    else:
        response = get_gemini_response(input_prompt, image)
        if response is not None:
            st.subheader("The Response is")
            st.write(response)

st.sidebar.title("Description")
st.sidebar.markdown("KanIQ is a web application utilizing Google's Generative AI to craft narratives from uploaded images and input prompts. Users upload images, provide prompts, and click 'Tell me about the image' to generate unique stories. The sidebar offers an example and guidance. Developed by [Kaniyamudhan Y](https://www.linkedin.com/in/kaniyamudhan-y/) for creative storytelling and AI exploration.  ")
st.sidebar.write("**Example:**")
st.sidebar.markdown("<em><strong>Input Prompt:</strong></em> <br>What dishes are in the image?", unsafe_allow_html=True)
st.sidebar.markdown("<em><strong>Choose an Image:</strong></em>", unsafe_allow_html=True)
st.sidebar.image("example_image.jpg", caption="Example Image", width=200) 
st.sidebar.markdown("<em><strong>Click:</strong></em> <br>The 'Tell me about the image' button to generate content.", unsafe_allow_html=True)
