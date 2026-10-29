# 🔧 AI Repair Assistant — PDF Chatbot Using RAG

🚀 **Live Demo:** [Click Here to Use AI Repair Assistant](https://rag-repair-assistant-vauutd92wdsbrs2emwm347.streamlit.app/)

An AI-powered repair assistant that allows users to upload PDF repair manuals and ask technical questions about their contents. It uses Retrieval-Augmented Generation (RAG), Gemini AI, HuggingFace embeddings, and FAISS to retrieve relevant information and generate context-aware answers.

## 🌐 Live Demo

👉 **Try the application:** https://rag-repair-assistant-vauutd92wdsbrs2emwm347.streamlit.app/

## 📌 Project Overview

The AI Repair Assistant makes it easier to understand technical repair manuals. Users can upload a PDF, ask questions in natural language, and receive answers based on information retrieved from the document.

Instead of manually searching through lengthy manuals, users can interact with their documents through an AI-powered chatbot.

## ✨ Features

- 📄 **PDF Upload:** Upload repair manuals in PDF format.
- 📝 **Text Extraction:** Extract text from uploaded PDF documents.
- ✂️ **Text Splitting:** Divide extracted text into smaller chunks.
- 🧠 **HuggingFace Embeddings:** Convert text into vector representations.
- 🔍 **FAISS Vector Database:** Retrieve relevant document sections.
- 🤖 **Gemini AI Integration:** Generate answers using retrieved information.
- 💬 **Question Answering:** Ask technical questions about repair manuals.
- 📌 **Source Page Detection:** Display relevant PDF page numbers when available.
- 🖥️ **Interactive Interface:** Navigate through Home, Upload PDF, Ask Question, and About pages.
- ⚙️ **Modular Code Structure:** Separate modules for document loading, splitting, embeddings, vector storage, and question answering.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | RAG pipeline and document processing |
| Google Gemini AI | AI-powered answer generation |
| HuggingFace | Text embedding generation |
| FAISS | Vector similarity search |
| PyPDF | PDF text extraction |
| Git and GitHub | Version control and project hosting |
| Streamlit Community Cloud | Application deployment |

## 🔄 How It Works

1. **Upload PDF:** The user uploads a repair manual.
2. **Extract Text:** The application reads the PDF and extracts its text.
3. **Split Documents:** The extracted text is divided into smaller chunks.
4. **Generate Embeddings:** Each chunk is converted into a vector representation.
5. **Create Vector Store:** FAISS indexes the embeddings for efficient similarity search.
6. **Ask a Question:** The user enters a technical question.
7. **Retrieve Context:** The system finds relevant document chunks.
8. **Generate an Answer:** Gemini AI generates a response using the retrieved context.
9. **Display Source Pages:** The application shows relevant PDF page numbers when available.

## 🏗️ RAG Architecture

```text
             PDF Repair Manual
                     |
                     v
              PDF Text Loader
                     |
                     v
               Text Splitter
                     |
                     v
          HuggingFace Embeddings
                     |
                     v
             FAISS Vector Store
                     |
                     v
               User Question
                     |
                     v
           Relevant Text Retrieval
                     |
                     v
                Gemini AI
                     |
                     v
             Generated Answer
                     |
                     v
           Answer + Source Pages
```

## 📂 Project Structure

```text
RAG-Repair-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .git
