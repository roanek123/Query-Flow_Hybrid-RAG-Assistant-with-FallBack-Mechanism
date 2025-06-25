import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from pydantic import SecretStr

# Load environment variables
load_dotenv()

# === Configuration ===

# Initialize the LLM (Google Gemini via OpenRouter)
llm = ChatOpenAI(
    model="mistralai/devstral-small:free",
    api_key=SecretStr("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"),
    base_url="https://openrouter.ai/api/v1"
)

# ✅ Use local HuggingFace Embeddings (no API required)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # or "BAAI/bge-base-en"

# Web search tool as fallback
search = DuckDuckGoSearchRun()


# === Vector Store Creation ===

def create_vector_store(pdf_file_paths):
    """Creates a FAISS vector store from a list of PDF file paths."""
    if not pdf_file_paths:
        return None

    docs = []
    for pdf_file_path in pdf_file_paths:
        loader = PyPDFLoader(pdf_file_path)
        docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # Create FAISS vector store
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
    return vectorstore


# === QA Retrieval ===

def get_answer(question, vectorstore):
    """Gets an answer from the RAG system or falls back to a web search."""
    if vectorstore:
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )
        result = qa_chain({"query": question})

        # If a confident answer is found
        if "I don't know" not in result["result"] and "I am not sure" not in result["result"]:
            return result["result"]

    # Fallback to DuckDuckGo web search
    return search.run(question)
