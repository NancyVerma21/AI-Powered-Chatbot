import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
import os

# Groq API key 
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY") 





st.header(" Groq PDF Chatbot")

with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload a PDF file", type="pdf")

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(chunks, embeddings)

    user_question = st.text_input("Ask your question")

    if user_question:
        docs = vector_store.similarity_search(user_question)

        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.1-8b-instant"
        )

        chain = load_qa_chain(llm, chain_type="stuff")

        response = chain.run(
            input_documents=docs,
            question=user_question
        )

        st.write(response)