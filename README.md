# QueryFlow AI – Hybrid RAG Assistant

**A voice-enabled Retrieval-Augmented Generation (RAG) system combining Gemini API, Hugging Face, Faiss, and ElevenLabs to deliver accurate, responsive, and human-like query answering via an elegant Streamlit interface.**

## Screenshots

![App Screenshot](https://github.com/roanek123/FashX--Multi-Agent-Fashion-Recommendation-using-AI-and-Knwledge-Base/blob/main/GRADIO%20PAGE.png)
---

## 🚀 Features

- 🔍 **Retrieval-Augmented Generation (RAG):**  
  Combines Gemini 1.5 API for response generation with Hugging Face transformer-based text embeddings.

- 📦 **Vector Store with Faiss:**  
  Stores and retrieves semantically relevant chunks from documents using Faiss for fast vector similarity search.

- 🌐 **Fallback to DuckDuckGo:**  
  If user query doesn’t match internal documents, system uses DuckDuckGo to fetch web context dynamically.

- 🗣️ **Text-to-Speech Integration (TTS):**  
  ElevenLabs API used to convert model responses into realistic audio, enhancing accessibility and engagement.

- 💻 **Streamlit UI:**  
  Interactive and modern frontend for querying, listening to results, and visualizing retrieved document matches.

---

## 📊 Performance

- ✅ Achieved **91% query resolution accuracy** on a benchmark set of 100 diverse questions.
- 🌐 Improved **out-of-domain query handling by 18%** using DuckDuckGo as fallback.
- 🔊 Reduced average response-to-audio latency to under **2.3 seconds**.

---

## 🧰 Tech Stack

| Component         | Technology Used         |
|------------------|-------------------------|
| LLM Inference    | Google Gemini 1.5 Pro, Msitral-Devstral  |
| Embeddings       | Hugging Face Transformers |
| Vector Store     | Faiss                   |
| Fallback Search  | DuckDuckGo Instant API  |
| TTS              | ElevenLabs API          |
| Frontend         | Streamlit               |
| Language         | Python                  |

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/queryflow-ai.git
   cd queryflow-ai
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install MPV (For Eleven labs text-to-speech)**
   ```bash
   install mpv from the website(https://mpv.io/installation/) and put the folder path in system varaibles PATH.
   ```

4. **Set Environment Variables**
   - `GEMINI_API_KEY`
   - `ELEVENLABS_API_KEY`
OR Hardcode the API_KEYS in your code.

5. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## 📁 Folder Structure

```
queryflow-ai/
│
├── app.py                    # Streamlit frontend logic
├── retriever.py              # Embedding + Faiss vector store logic
├── .env                      # API keys, secrets 
└── requirements.txt
```

---

## 📌 Future Improvements

- Add other document ingestion pipeline
- Add multilingual support for queries and TTS
- Enable real-time microphone input for voice-based querying

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share with attribution.

