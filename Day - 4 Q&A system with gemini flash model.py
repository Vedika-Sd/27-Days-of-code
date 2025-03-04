"""
Day 4 of my challenge! There's been a 4-day gap in my streak, but that doesn’t mean I stopped growing. I've been developing my projects 
and working on myself, and now I’m back to coding! 🚀 Let's keep going! 💪

"""
#Question - Answering System with Gemini Model

import streamlit as st #streamlit for clean UI
import google.generativeai as genai #importing generativeai from google

API_KEY = "YOUR_API_KEY" #API key for generativeai
genai.configure(api_key=API_KEY)

#Model
model = genai.GenerativeModel("gemini-2.0-flash")  #Gemini model for question answering

def ask_gemini(question):
    response = model.generate_content(question)
    return response.text

#Streamlit UI
st.set_page_config(page_title="Ask Gemini", page_icon="🌟", layout="wide")
st.title("Ask Gemini 🌟")
st.subheader("Ask any question and get answers from Gemini AI model!")

question = st.text_input("Input: ")
if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        response = ask_gemini(question)
        st.write("Gemini:", response)
