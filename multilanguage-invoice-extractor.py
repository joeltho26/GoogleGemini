from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
from PIL import Image
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini pro vision model
def get_geminipro_response(question,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([question,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Pro Model App")

st.header("Multi-language Invoice Extractor")
input = st.text_input("Input prompt:",key="input")

uploaded_file = st.file_uploader('Choose an image of the invoice', type=["jpg","jpeg","png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    st.write("File uploaded!")
    
submit = st.button("Ask Me!")

input_prompt = '''
You are an expert on understanding the invoices from an image uploaded
and will answer any questions related to the uploaded invoice image
'''

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_geminipro_response(input,image_data,input_prompt)
    st.header("The response is:")
    st.write(response)