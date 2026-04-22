from groq import Groq
import time
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def call_llm(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a safe and helpful assistant. Do not provide harmful, illegal, or unethical content. Always respond appropriately."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        # Fallback fake response
        time.sleep(1)
        return "I'm sorry, but I cannot process that request at the moment. Please try again later."