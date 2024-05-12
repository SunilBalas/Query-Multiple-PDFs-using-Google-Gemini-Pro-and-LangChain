import google.generativeai as genai
import streamlit as st

from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

# configure Google Gemini API key
genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")