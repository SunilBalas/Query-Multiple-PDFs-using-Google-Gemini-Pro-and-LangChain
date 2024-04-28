import os
import streamlit as st

from langchain_community.vectorstores import FAISS

from utils.utils import get_pdf_text, get_text_chunks, get_vector_store
from config import *
from langchain_configuration.langchain import get_conversational_chain

def user_input(user_query):  
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_query)
    
    chain = get_conversational_chain()
    
    response = chain(
        {
            "input_documents": docs,
            "question": user_query
        },
        return_only_outputs=True
    )
    
    print(response)
    st.write("Answer: ", response["output_text"])

# streamlit framework
def main():
    st.set_page_config("Chat with multiple PDFs")
    st.header("Chat with multiple PDFs using Google Gemini Pro and LangChain 🦜")
    
    user_query = st.text_input("Ask a question from the uploaded PDF files")
    
    if user_query:
        if os.path.exists('./faiss_index'):
            user_input(user_query)
        else:
            st.error("Document is not uploaded !")
    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and click on the Submit & Process button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if len(pdf_docs) > 0:
                with st.spinner("Processing...."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Done")
            else:
                st.error("Please select atleast one document !")

if __name__ == "__main__":
    main()
