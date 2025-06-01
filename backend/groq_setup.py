import os
import httpx
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def generate_sql_query(user_input: str) -> str:
    prompt = f"""
                You are an expert in SQL. Given a natural language query, generate a SQL query for this customer database:

                Table: customers
                Columns: customer_id (int), name (text), gender (text), location (text)

                Use exact values from the gender column: 'Male' or 'Female' (not 'M' or 'F').

                Only return the SQL query. Do not include explanations, assumptions, or formatting like triple quotes.

                Natural language query: {user_input}
                """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama3-8b-8192"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
