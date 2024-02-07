import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# GeminiPro model and response function
def get_geminipro_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response

st.set_page_config(page_title="Gemini Pro Application")
st.header("Gemini Pro Q&A Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input = st.text_input("Input",key="input")
submit = st.button("Submit")

if submit and input:
    response = get_geminipro_response(input)
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
        
st.subheader("Chat History")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")