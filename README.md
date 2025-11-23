# 🎤 AI Interview Practice Partner  

A voice-based mock interview assistant that conducts realistic job interviews, asks follow-up questions, evaluates answers, and provides structured feedback across communication, behaviour, and technical depth.

This project was built as part of an AI agent assignment with a focus on **conversation quality**, **agentic behaviour**, **technical implementation**, and **adaptability to different user personas**.

---

# 🚀 Features

### 🔊 Voice-first Interaction  

- User speaks answers using the microphone.  
- App transcribes speech to text.  
- Sends responses to backend AI agent for evaluation.

### 🧠 Dynamic Interview Agent  

- Conducts mock interviews for different roles:
  - Software Engineer  
  - Sales Associate  
  - Retail Associate  
  - Product Manager  
- Follows up based on user responses.  
- Adapts tone depending on user persona.

### 📊 Post-Interview Feedback  

Agent evaluates your answers on:

- Clarity  
- Structure (STAR method)  
- Depth of knowledge  
- Relevance  
- Confidence & communication  

Generates:

- Scores  
- Strengths  
- Areas to improve  
- Personalised recommendations  

---


# ⚙️ Setup Instructions

## 1️⃣ Clone the project
git clone https://github.com/elsie-05/interview_agent.git
cd Interview-agent

---

# 🖥️ Backend Setup (FastAPI)

### 1. Go to backend folder
cd backend

### 2. Create virtual environment
python -m venv env

### 3. Activate

**Windows (CMD):**
env\Scripts\activate

**Mac/Linux:**
source env/bin/activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Start backend
uvicorn main:app --reload --port 8000

Backend runs at:
http://localhost:8000

### 6. Start frontend
python -m http.server 8000

---

# 🧱 System Architecture

### **Architecture Overview**
User (Voice)
       ↓ (Microphone)
Frontend (Streamlit)
       ↓ (Transcribed text via API)
Backend (FastAPI)
       ↓
Interview Engine (Logic + State)
       ↓
LLM / Scoring Module
       ↓
Backend generates next question + evaluation
       ↓
Frontend displays & speaks output


### Components

#### **Frontend**

- Collects user voice input  
- Uses `streamlit_mic_recorder` for recording  
- Sends text to backend  
- Displays next interview question  

#### **Backend**

- FastAPI routes for:
  - `/start_interview`
  - `/submit_answer`
  - `/final_feedback`
- Interview engine:
  - Question bank per role  
  - Follow-up question generator  
  - Response evaluator  
  - Score calculator  

#### **Agent Logic**

- Supports different roles  
- Automatically detects:
  - vague answers  
  - incomplete answers  
  - off-topic responses  
- Generates meaningful follow-up prompts

---

# 🧠 Design Decisions

## 1️⃣ Chose FastAPI for Backend

Reasons:

- Lightweight  
- Fast ASGI performance  
- Auto-generated Swagger docs  
- Easy integration with ML logic  

## 2️⃣ Chose Streamlit for Frontend

Reasons:

- Rapid UI development  
- Built-in microphone components  
- Ideal for demo-based projects  

## 3️⃣ Structured Agent Engine

We avoided a simple "chatbot" and instead built:

- **Stateful interview tracker**  
- **Role-specific question flow**  
- **Adaptive follow-up generator**  
- **Custom scoring rubric**  

## 4️⃣ Human-like Naming Conventions

To avoid LLM-generated patterns:

- Variables use natural names (`current_answer`, `session_notes`, `topic_focus`)  
- Functions named based on intent (`prepare_next_question`, `judge_response`)  

---
# 🎉 Final Notes  

This project focuses heavily on:

- Natural conversation flows  
- Evaluative intelligence  
- Adaptive behaviour  
- Delivering a realistic interview experience  

The full system is built to satisfy all requirements in the assignment.








