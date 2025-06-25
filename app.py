import streamlit as st
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
import os
import shutil
from dotenv import load_dotenv
from rag_system import create_vector_store, get_answer

load_dotenv()

# ElevenLabs setup


client = ElevenLabs(api_key="sk_75d3ee6130a5fe97bcfdefd3feebf7d420e41e95dc3780c1")

def text_to_speech(text):
    """Converts text to speech and streams it."""
    try:
        # Using a default voice, you can find more voice_ids in your ElevenLabs account
        audio_stream = client.text_to_speech.convert(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            text=text
        )
        stream(audio_stream)
    except Exception as e:
        st.error(f"Error during text-to-speech conversion: {e}")

st.title("RAG-based Question Answering System")

# Sidebar for document upload
st.sidebar.title("Upload Documents")
uploaded_files = st.sidebar.file_uploader(
    "Upload your PDF documents",
    accept_multiple_files=True,
    type="pdf"
)

if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None

if uploaded_files:
    temp_dir = "temp_uploaded_files"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    file_paths = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(file_path)

    with st.spinner("Processing documents and creating vector store... This may take a moment."):
        st.session_state.vector_store = create_vector_store(file_paths)
    
    st.sidebar.success("Documents processed and vector store is ready!")

    # Clean up temporary files
    shutil.rmtree(temp_dir)

# Main interface for asking questions
st.header("Ask a Question")
question = st.text_input("Enter your question here:")

if question:
    if st.session_state.vector_store is None:
        st.warning("Please upload documents first to ask questions based on them. The answer will be from a web search.")
    
    st.write(f"You asked: {question}")
    with st.spinner("Searching for the answer..."):
        answer = get_answer(question, st.session_state.vector_store)
    
    st.subheader("Answer:")
    st.write(answer)

    if st.button("Listen to the Answer"):
        text_to_speech(answer) 