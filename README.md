# 🚀 RAG-based Assistant for Videos

![GitHub stars](https://img.shields.io/github/stars/Dhairya1000/RAG-based-Assistant-for-videos-?style=for-the-badge&logo=github)
![GitHub forks](https://img.shields.io/github/forks/Dhairya1000/RAG-based-Assistant-for-videos-?style=for-the-badge&logo=github)
![GitHub issues](https://img.shields.io/github/issues/Dhairya1000/RAG-based-Assistant-for-videos-?style=for-the-badge&logo=github)

---

## 📌 Overview

**RAG-based Assistant for Videos** is an AI-powered system that allows users to **chat with video content**.  
It uses a **Retrieval-Augmented Generation (RAG)** pipeline to extract, index, and retrieve meaningful insights from videos.

Instead of manually watching long videos, users can ask questions and get **accurate, context-aware answers instantly**.

---

## ✨ Features

- 🎥 Convert video → text using Whisper  
- 🧠 Semantic search using embeddings  
- 💬 Ask questions about video content  
- ⚡ Fast and accurate retrieval (RAG pipeline)  
- 📂 JSON-based transcript storage  
- 🧩 Modular architecture  

---

## 🛠️ Tech Stack

- **Language:** Python 🐍  
- **Speech-to-Text:** OpenAI Whisper  
- **LLM Runtime:** Ollama  
- **Architecture:** RAG (Retrieval-Augmented Generation)  
- **Storage:** JSON  

---

## ⚙️ How It Works

1. 🎬 Input video file  
2. 🔊 Extract audio + generate transcript (Whisper)  
3. ✂️ Split transcript into chunks  
4. 🧠 Generate embeddings  
5. 🔍 Retrieve relevant chunks based on query  
6. 🤖 Generate answer using Ollama  

---

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/Dhairya1000/RAG-based-Assistant-for-videos-.git

# Go to project folder
cd RAG-based-Assistant-for-videos-

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
# Step 1: Process video
python process_video.py

# Step 2: Ask questions
python process_question.py
```

--

## 📁 Project Structure

```bash
.
├── create_chunk_of_audios.py
├── create_embeddings.py
├── process_video.py
├── process_question.py
├── jsons/
```

---

## 🎯 Use Cases

- 📚 Learn from lecture videos faster  
- 🔬 Research long recordings  
- 🎬 Extract insights from content  
- 💼 Analyze meetings/webinars  

---

## 🚀 Future Improvements

- 🌐 Web UI (Streamlit / React)  
- 📊 Vector DB (FAISS / Chroma)  
- 🔎 Multi-video support  
- 🎙️ Real-time processing  

---

## 🤝 Contributing

```bash
# Fork repo
# Create branch
git checkout -b feature/your-feature

# Commit changes
git commit -m "Added new feature"

# Push
git push origin feature/your-feature
```

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
