# Smart Interaction Management System : AI-First CRM – HCP Interaction Module

## Overview

AI-First CRM is a Healthcare Professional (HCP) Customer Relationship Management system designed for Life Science field representatives. The application enables users to log interactions with healthcare professionals using either:

* **Structured Form Interface**
* **AI-powered Conversational Chat Interface**

The AI assistant is built using **LangGraph** and **Groq LLM**, allowing natural language interaction while automatically extracting structured information and storing it in the CRM database.

---

## Assignment Objective

This project was developed as part of the AI-First CRM HCP Module assignment.

The objective is to build an intelligent CRM interaction logging system that combines traditional form-based data entry with an AI assistant capable of understanding natural language and performing CRM operations.

---
## Simple Architecture Diagram:

```text
                 React + Redux
                       │
               REST API (FastAPI)
                       │
               LangGraph Agent
                       │
     ┌──────────┬──────────┬──────────┐
     │          │          │          │
 Log Tool   Edit Tool  Search Tool  History Tool
     │
 PostgreSQL Database

```

---


## Features

### Structured Interaction Logging

* Log meetings with Healthcare Professionals
* Record interaction date and time
* Interaction type
* Topics discussed
* Materials shared
* Samples distributed
* Outcomes
* Follow-up actions
* Sentiment

---

### AI Chat Assistant

Users can interact naturally with the CRM.

Example:

> "I met Dr Rahul Sharma today and discussed Ozempic. He was interested and asked me to follow up after two weeks."

The AI automatically extracts:

* Doctor
* Interaction Type
* Date
* Time
* Topics
* Sentiment
* Follow-up
* Outcomes

and stores the interaction in PostgreSQL.

---

## AI Agent (LangGraph)

The application uses **LangGraph** to orchestrate the AI workflow.

### Workflow

User Message

↓

Intent Classification

↓

Route to Appropriate Tool

↓

Database Operation

↓

AI Response

---

## LangGraph Tools

The AI Agent currently supports the following tools:

### 1. Log Interaction

* Extracts structured interaction information from natural language.
* Creates interaction records in PostgreSQL.

---

### 2. Edit Interaction

Allows updating existing interaction records.

Example:

> "Change the sentiment of Dr Rahul Sharma to Neutral."

---

### 3. Search HCP

Searches Healthcare Professionals by name.

Example:

> "Find Dr Rahul Sharma"

---

### 4. Interaction History

Retrieves all previous interactions with an HCP.

Example:

> "Show interaction history of Dr Rahul Sharma"

---

### 5. Follow-up Tool

Lists all pending follow-up activities.

Example:

> "Who needs follow up?"

---

## Technology Stack

### Frontend

* React
* Redux Toolkit
* Google Inter Font

### Backend

* Python
* FastAPI

### AI

* LangGraph
* LangChain
* Groq API
* Llama 3.3 70B Versatile

### Database

* PostgreSQL
* SQLAlchemy

---

## Project Structure

```text
AI-First-CRM/

├── backend/
│
│   ├── agent/
│   │      ├── graph.py
│   │      ├── nodes.py
│   │      ├── state.py
│   │      └── tools.py
│   │
│   ├── app/
│   │      ├── routers/
│   │      ├── models.py
│   │      ├── schemas.py
│   │      ├── crud.py
│   │      ├── database.py
│   │      └── main.py
│   │
│   ├── services/
│   │      └── groq_service.py
│   │
│   └── requirements.txt
│
└── frontend/
```

---

## REST APIs

### HCP APIs

| Method | Endpoint       | Description  |
| ------ | -------------- | ------------ |
| GET    | `/hcps`        | Get all HCPs |
| GET    | `/hcps/search` | Search HCP   |

---

### Interaction APIs

| Method | Endpoint                         | Description          |
| ------ | -------------------------------- | -------------------- |
| GET    | `/interactions`                  | Get all interactions |
| POST   | `/interactions`                  | Create interaction   |
| GET    | `/interactions/history/{hcp_id}` | Interaction history  |
| GET    | `/interactions/followups`        | Pending follow-ups   |

---

### AI API

| Method | Endpoint | Description                 |
| ------ | -------- | --------------------------- |
| POST   | `/chat`  | Conversational AI interface |

---

## Setup

### Clone Repository

```bash
git clone <repository-url>

cd AI-First-CRM
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5433/ai_first_crm

GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

### Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

---

## Sample AI Commands

Log interaction

> I met Dr Rahul Sharma today and discussed Ozempic.

Edit interaction

> Change the sentiment of Dr Rahul Sharma to Neutral.

Search doctor

> Find Dr Rahul Sharma.

Interaction history

> Show interaction history of Dr Rahul Sharma.

Follow-up

> Who needs follow up?

---

## Demo

### 1. API Overview (Swagger)
![API overview](https://github.com/LajinaD/AI-First-CRM/blob/0ac451edb57f4477197f683618f80393b0107657/Screenshot%202026-07-24%20213620.png)

*All REST and AI endpoints exposed via FastAPI's interactive docs*

### 2. AI Chat — Logging an Interaction
![Chat logging demo](https://github.com/LajinaD/AI-First-CRM/blob/a4c6151e85051437be6a040dc23707a8e0fdd729/Screenshot%202026-07-25%20123727.png)
![Chat logging demo](https://github.com/LajinaD/AI-First-CRM/blob/a4c6151e85051437be6a040dc23707a8e0fdd729/Screenshot%202026-07-25%20123815.png)

*Natural language input parsed into structured CRM data by the LangGraph agent*

### 3. AI Chat — Editing a Record
![Chat edit demo](./screenshots/edit-demo.png)

*Follow-up command updating a previously logged interaction*



## Future Enhancements

* Authentication & Authorization
* Dashboard Analytics
* HCP Profile Management
* Email Integration
* Calendar Scheduling
* AI-generated Visit Summaries
* RAG-enabled Medical Knowledge Assistant
* Voice-based Interaction Logging

---

## Developed By

Assignment Submission – AI-First CRM HCP Module

Built using:

* FastAPI
* PostgreSQL
* LangGraph
* Groq LLM
* React
* Redux
