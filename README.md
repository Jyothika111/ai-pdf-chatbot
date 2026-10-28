# 🤖 AI PDF Chatbot

An AI-powered PDF chatbot that allows users to upload PDF documents and ask questions about their content using natural language. It uses document processing, vector embeddings, and Retrieval-Augmented Generation (RAG) to generate relevant answers.

## ✨ Features

- 📄 Upload PDF documents
- 💬 Ask questions about uploaded documents
- 🧠 AI-powered question answering
- 🔎 Text extraction and OCR fallback for scanned documents
- 📚 Document chunking and vector search
- 🌐 Simple, responsive web interface

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **AI:** Google Gemini API
- **Document Processing:** PDF text extraction and OCR
- **Vector Database:** ChromaDB
- **Embeddings:** Text embeddings for semantic search

## 📁 Project Structure

```text
ai-pdf-chatbot/
├── backend/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── ocr_reader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   └── llm.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The file list above is illustrative; keep only paths that actually exist in your project.*

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-pdf-chatbot.git
cd ai-pdf-chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root or the location expected by your backend, and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Use the exact variable name your backend reads. Never commit your real API key.

### 5. Run the backend

From the project root, enter the backend folder:

```powershell
cd backend
uvicorn main:app --reload
```

### 6. Run the frontend

In a separate terminal, from the project root, run:

```powershell
python -m http.server 5500 --directory frontend
```

Open `http://127.0.0.1:5500` in your browser.

## 🔐 Security

- Keep API keys in environment variables.
- Do not upload `.env` files, private PDFs, or virtual environment folders.
- Validate uploaded files before processing.

## 🚀 Future Improvements

- Deploy the frontend and backend online.
- Improve handwritten text recognition.
- Add support for multiple documents and chat history.
- Improve error handling and document retrieval accuracy.

## 👩‍💻 Author

**YOUR NAME**

S Gayathri Jyothika

## 📄 License

Choose and add a license if you intend to distribute this project under specific open-source terms.
