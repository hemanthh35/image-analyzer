# 🧠 Local Image Analyzer using FastAPI + Ollama (LLaVA)

Analyze images locally using a vision-language model (LLaVA) powered by [Ollama](https://ollama.com/). Upload an image through the frontend or Postman and get a detailed description — all running locally without internet or API keys.

---

## 📸 Features

* 🔍 Analyze images using LLaVA locally
* ⚡ FastAPI backend for handling image uploads
* 🌐 Simple HTML frontend
* 𞳁 No cloud, no API keys, runs entirely on your machine
* 🧪 Easy to test with Postman

---

## ✨ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hemanthh35/image-analyzer.git
cd image-analyzer
```

### 2️⃣ Start LLaVA Model Locally

> Requires [Ollama](https://ollama.com/) installed

```bash
ollama run llava
```

### 3️⃣ Start FastAPI Server

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn backend.main:app --reload
```

### 4️⃣ Open Frontend

Just open:

```text
frontend/index.html
```

> Or serve it with a static server:
> `python -m http.server 8080`

---

## 🦪 Test with Postman

* **Method**: `POST`
* **URL**: `http://127.0.0.1:8000/analyze`
* **Body** → `form-data` → `file`: (choose an image)

---

## 📁 Project Structure

```
image-analyzer/
├── backend/
│   └── main.py            # FastAPI backend
├── frontend/
│   └── index.html         # Simple frontend UI
├── requirements.txt
└── .gitignore
```

---

## 🧰 Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [Ollama](https://ollama.com/)
* [LLaVA Model](https://llava-vl.github.io/)
* HTML + JS

---

## 📜 License

MIT License — use freely, modify boldly.

---

## 🙌 Acknowledgments

* Thanks to [Ollama](https://ollama.com/) for making local LLMs accessible.
