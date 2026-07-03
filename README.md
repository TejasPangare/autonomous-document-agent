# 🤖 Autonomous Document Agent

An AI-powered autonomous document generation system built with **FastAPI** that understands natural language requests, creates its own execution plan, generates professional business documents, reviews them for quality, and exports them as Microsoft Word (`.docx`) files.

## 🚀 Features

- 📝 Accepts natural language requests
- 🧠 Autonomous planning using an LLM
- 📋 Generates an execution/task plan
- ✍️ Executes the plan to generate structured documents
- 🔍 Reflection-based review for improved document quality
- 📄 Exports professional Microsoft Word (`.docx`) documents
- ⚡ REST API built using FastAPI
- 🔄 Modular Planner → Executor → Reviewer architecture
- 🆓 Uses free/open-source LLMs (Groq/Gemini configurable)

---

## 🏗️ Architecture

```
                    User Request
                          │
                          ▼
                  Request Validator
                          │
                          ▼
                 Planner Agent (LLM)
                          │
                          ▼
                  Execution Plan
                          │
                          ▼
                 Writer Agent (LLM)
                          │
                          ▼
               Structured Document
                          │
                          ▼
               Reviewer Agent (LLM)
                          │
                          ▼
                Document Generator
                  (python-docx)
                          │
                          ▼
                  Generated DOCX
```

---

## 📂 Project Structure

```
autonomous-document-agent/

├── app/
│   ├── agent/
│   │   ├── planner.py
│   │   ├── executor.py
│   │   └── reviewer.py
│   │
│   ├── llm/
│   │   ├── factory.py
│   │   ├── groq.py
│   │   └── gemini.py
│   │
│   ├── prompts/
│   │   ├── planner.py
│   │   ├── writer.py
│   │   └── reviewer.py
│   │
│   ├── tools/
│   │   ├── writer_tool.py
│   │   └── document_tool.py
│   │
│   ├── utils/
│   │   └── parser.py
│   │
│   ├── models.py
│   ├── config.py
│   └── main.py
│
├── outputs/
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/TejasPangare/autonomous-document-agent.git

cd autonomous-document-agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

Example:

```env
LLM_PROVIDER=groq

GROQ_API_KEY=YOUR_API_KEY
```

(Alternatively configure Gemini if desired.)

---

## ▶️ Run

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API

### POST `/agent`

Request

```json
{
    "request":"Create a business proposal for implementing an Employee Attendance Management System."
}
```

Response

```json
{
    "status":"success",
    "document_path":"outputs/business_proposal.docx"
}
```

---

## 🧠 Agent Workflow

### Planner

- Understands the user's request
- Makes assumptions when information is missing
- Creates an execution plan
- Generates document sections

### Writer

- Uses the execution plan
- Generates structured business document content

### Reviewer

- Reviews the generated document
- Improves grammar, completeness, and professional tone

### Document Generator

- Converts structured content into a Microsoft Word document
- Saves the generated document locally

---

## 🛠️ Tech Stack

- Python 3.12+
- FastAPI
- Pydantic
- Groq API (or Gemini)
- python-docx
- Uvicorn

---

## 📄 Sample Documents

The agent can generate:

- Business Proposals
- Project Proposals
- Technical Design Documents
- Product Specifications
- Standard Operating Procedures (SOPs)
- Business Reports
- Meeting Minutes

---

## ⭐ Engineering Improvement

This project implements **Reflection / Self-Review**.

After generating the initial document, a Reviewer Agent evaluates it for:

- Completeness
- Professional tone
- Grammar
- Missing sections
- Overall quality

The reviewed document is then exported as the final `.docx` file.

---

## 📈 Future Improvements

- Multi-agent execution
- Tool calling
- Retrieval-Augmented Generation (RAG)
- Conversation memory
- PDF export
- Web UI
- Template-based document generation
- Cloud storage integration

---

## 👨‍💻 Author

**Tejas Pangare**

GitHub: https://github.com/TejasPangare

LinkedIn: https://www.linkedin.com/in/tejas-pangare-a65537279

---

## 📜 License

This project is developed for learning and technical assessment purposes.
