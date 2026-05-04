# Guardrail System for LLM Applications

## 📌 Overview

This project implements a basic AI safety layer (guardrail system) for Large Language Models (LLMs). It focuses on preventing unsafe or malicious inputs from reaching the model and filtering unsafe outputs.

The system demonstrates how to build a controlled AI interaction pipeline using rule-based filtering techniques.

---

## 🎯 Features

* Input guardrails (keyword-based filtering)
* Output guardrails (response validation)
* Prompt injection detection (basic patterns)
* Flask-based backend API
* Local or API-based LLM integration

---

## 🧠 Architecture

User Input → Input Filter → LLM → Output Filter → Response

---

## ⚙️ Tech Stack

* Python
* Flask
* Rule-based filtering
* LLM (API or local via Ollama)

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python app.py
```

Open:
http://127.0.0.1:5000

---

## 🧪 Example

### Unsafe Input:

How to hack a system
→ ❌ Blocked

### Safe Input:

Explain AI
→ ✅ Response generated

---

## ⚠️ Limitations

* Relies on keyword-based filtering
* Cannot detect semantic variations of unsafe prompts
* Vulnerable to paraphrased attacks
* Limited adaptability

---

## 📚 Learning Outcome

* Understanding guardrails
* Prompt injection basics
* Layered AI safety approach

---
