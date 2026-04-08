# AI-Powered PDF Chatbot with RAG

A conversational chatbot that lets you upload a PDF and ask questions about its content using Groq's LLaMA model.

## Features
- Upload any PDF file
- Ask questions in natural language
- Powered by Groq LLaMA 3.1 (fast AI responses)
- Uses FAISS for smart document search

## Tech Stack
- Python
- Streamlit (UI)
- LangChain
- HuggingFace Embeddings
- FAISS Vector Store
- Groq API

## Setup Instructions

1. Clone the repository
   git clone https://github.com/NancyVerma21/AI-Powered-Chatbot.git

2. Install dependencies
   pip install -r requirements.txt

3. Create a .env file and add your Groq API key
   GROQ_API_KEY=your_api_key_here

4. Run the app
   streamlit run chatbot.py

## Get Groq API Key
Sign up free at https://console.groq.com
