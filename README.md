# 🪿 GusiniAI

<p align="center">

A modern AI assistant powered by Google Gemini with a custom FastAPI backend and an Apple-inspired user interface.

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python">
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi">
<img src="https://img.shields.io/badge/Google-Gemini-orange?logo=google">
<img src="https://img.shields.io/badge/License-MIT-green">

</p>


## ✨ About

**GusiniAI** is a personal AI assistant built from scratch using Python and Google Gemini.

The project combines a modern web interface with a lightweight FastAPI backend to provide a simple and elegant AI chat experience.

The goal of GusiniAI is to create a clean, fast and extensible AI assistant architecture that can be improved with new features over time.


## 🚀 Features

### 💬 AI Chat
- Powered by Google Gemini API
- Fast response generation
- Conversation history storage

### 🎨 Modern Interface
- Apple-inspired minimalistic design
- Responsive layout
- Smooth animations
- Empty chat state
- Auto-growing input field

### 📝 Smart Message Rendering
- Markdown support
- Code blocks formatting
- Lists and headings
- Copy assistant responses

### ⚙️ Backend
- FastAPI REST API
- SQLAlchemy database layer
- Environment variable configuration
- Modular project structure


## 🖥️ Screenshots

<p align="center">

<img src="screenshots/main.png" width="800">

</p>


## 🏗️ Project Structure
GusiniAI/

├── backend/
│
│ ├── main.py # FastAPI application
│ ├── gemini_client.py # Gemini API integration
│ ├── db.py # Database models and queries
│ ├── config.py # Configuration
│ ├── requirements.txt # Dependencies
│ └── .env.example # Environment template
│
├── frontend/
│
│ └── index.html # Web interface
│
├── README.md
├── LICENSE
└── .gitignore



## 🛠️ Technologies

### Frontend
- HTML
- CSS
- JavaScript
- Markdown rendering

### Backend
- Python
- FastAPI
- SQLAlchemy
- Google Gemini API

### Database
- SQLite


## ⚡ Installation


### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/GusiniAI.git

cd GusiniAI

2. Create virtual environment
python -m venv .venv

Activate:

Windows:

.venv\Scripts\activate

Linux / macOS:

source .venv/bin/activate
3. Install dependencies
pip install -r backend/requirements.txt
4. Configure environment variables

Create:

backend/.env

Add your Gemini API key:

API_KEY=your_gemini_api_key
5. Run backend
cd backend

uvicorn main:app --reload

The API will start at:

http://localhost:8000
6. Run frontend

Open:

frontend/index.html

or use a local web server.

🔌 API Endpoints
Get chat history
GET /requests
Send message
POST /requests

Example:

{
  "prompt": "Explain Python decorators"
}

Response:

{
  "answer": "..."
}
🗺️ Roadmap
 Gemini integration
 FastAPI backend
 Chat history
 Modern UI
 Markdown rendering
 Copy messages

Future:

 Streaming responses
 User authentication
 PostgreSQL support
 Docker deployment
 Public cloud deployment
📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Created by Max Repka

⭐ If you find this project interesting, consider giving it a star!