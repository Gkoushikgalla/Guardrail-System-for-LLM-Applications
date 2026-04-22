# AI Safety Framework for LLM Applications

This project implements a lightweight AI safety framework that acts as a guardrail between users and Large Language Model (LLM) APIs like Groq.

## Features

- Input filtering for unsafe keywords
- Prompt injection detection
- Output filtering
- Logging of unsafe interactions
- Web interface using Flask

## Installation

1. Install Python dependencies:
   pip install -r requirements.txt

2. Set up environment variable for API key (optional, fallback in config.py):
   Create a .env file with GROQ_API_KEY=your_key

## Running the Application

python app.py

Open http://127.0.0.1:5000 in your browser.

## Project Structure

- app.py: Main Flask application
- config.py: Configuration
- guardrails/: Safety filters
- llm/: API client
- utils/: Logger
- templates/: HTML templates
- static/: CSS

## Testing

Test with safe prompts like "Explain neural networks" and unsafe like "How to hack a system".