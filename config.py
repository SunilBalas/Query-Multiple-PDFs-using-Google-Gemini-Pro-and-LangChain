import os
import google.generativeai as genai

from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# load all the environment variables
load_dotenv()

# configure Google Gemini API key
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")