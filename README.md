# Guardrail-System-for-LLM-Applications

## 📌 Overview

This project is a foundational AI safety system that introduces the concept of guardrails for Large Language Models (LLMs). It focuses on controlling unsafe inputs and outputs using rule-based filtering techniques.

This project serves as the **baseline version**, highlighting both the strengths and limitations of traditional guardrail systems.

---

## 🎯 Features

* Keyword-based input filtering
* Basic prompt injection detection
* Output validation layer
* Flask-based API system
* LLM integration (API or local)

---

## 🧠 Architecture

User Input → Input Guardrail → LLM → Output Guardrail → Response

---

## ⚙️ Tech Stack

* Python
* Flask
* Rule-based filtering
* LLM (API / local via Ollama)

---

## 🧪 Example

### Unsafe Input:

How to hack a system
→ ❌ Blocked

### Safe Input:

Explain AI
→ ✅ Response generated

---

## ⚠️ Limitations (Addressed in SafePrompt v2)

### 1. Keyword-Based Detection Only

* This system relies on exact keyword matching.
* ❌ Easily bypassed using paraphrased inputs.

👉 In **SafePrompt v2**, this is solved using **semantic similarity (embedding-based detection)**.

---

### 2. Weak Against Adversarial Prompts

* Indirect or disguised malicious intent is not detected.

👉 In **SafePrompt v2**, intent is analyzed using **semantic filtering**, making it robust against adversarial phrasing.

---

### 3. No Deep Understanding of Context

* Cannot differentiate between safe and unsafe variations of similar queries.

👉 In **SafePrompt v2**, contextual similarity improves decision-making.

---

### 4. Limited Real-World Robustness

* Not suitable for production-level safety systems.

👉 In **SafePrompt v2**, the architecture is redesigned with **layered and modular safety logic**.

---

## 📚 Learning Outcome

* Fundamentals of AI guardrails
* Prompt injection basics
* Rule-based safety systems

---

## 🔄 Evolution

This project directly led to the development of:

➡️ **SafePrompt v2: Semantic AI Safety Gateway**

which addresses its core limitations using semantic intelligence and improved architecture.
