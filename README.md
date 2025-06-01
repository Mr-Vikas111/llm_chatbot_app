# 💬 LLM-Powered Chatbot with FastAPI and SQL Integration

This project is a simple yet powerful chatbot application that leverages an LLM (via Groq API) to convert natural language queries into SQL commands. It retrieves relevant data from a customer database and displays it via a React frontend.

---

## 🚀 Features

- Convert natural language queries into SQL using Groq-hosted LLMs (LLaMA 3.1)
- Execute generated SQL on a customer database (PostgreSQL)
- Display results through a React UI
- Error handling and logging for debugging
- API key configuration via `.env`
- Optional: Token-based API security

---

## 🧱 Tech Stack

| Component   | Technology       |
|-------------|------------------|
| Backend     | FastAPI (Python) |
| Frontend    | ReactJS          |
| Database    | PostgreSQL |
| LLM API     | Groq (Free Tier) |

---

## 📁 Project Structure
<pre>
chatbot_app/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── groq_client.py
│ ├── utils.py
│ ├── seed.py
│ └── .env
├── frontend/
│ ├── public/
│ └── src/
│ ├── App.js
│ ├── App.css
│ └── index.js
│ └── .env
├── README.md
└── requirements.txt
</pre>


---

## ⚙️ Backend Setup (FastAPI)

### 🔹 Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### 🔹 Installation Steps

```bash
# Navigate to backend folder
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r ../requirements.txt
```

### 🔹 Environment Variables

Create a .env file in the backend/ directory:

```env
GROQ_API_KEY=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
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=YOUR_DB_NAME
POSTGRES_USER=YOUR_DB_USER
POSTGRES_PASSWORD=YOUR_DB_PASSWORD
```
Note:- key will be disable after 24 Hrs.

### 🔹 Seed the Database

```base
python seed.py
```

### 🔹 Run the FastAPI Server

```base
uvicorn main:app --reload
```

### 🔹 Example cURL Request
To send a POST request to the `/query` endpoint with a JSON payload:

```bash
curl -X POST http://localhost:8000/query \
     -H "Content-Type: application/json" \
     -d '{"user_query": "Show me all female customers from Mumbai" }'

```
Payload

```json
{
  "user_query": "Show me all female customers from Mumbai"
}
```

Response

```json
{
    "sql": "SELECT * \nFROM customers \nWHERE gender = 'Female' AND location = 'Mumbai';",
    "results": [
        [
            3,
            "Megha",
            "Female",
            "Mumbai"
        ]
    ]
}

```


# 🌐 Frontend Setup (React)

### 🔹 Prerequisites

- Node.js and npm

### 🔹 Installation Steps

``` # Navigate to frontend folder
cd ../frontend

# Install dependencies
npm install
```

### 🔹 Environment Variables

Create a .env file in the frontend/ directory:

```env
REACT_APP_API_URL=http://localhost:8000
```

### 🔹 Start the React App

```base
npm start
```

The frontend will be available at http://localhost:3000.

# 🧪 Usage Example

Type a natural language query like:

```sql
Show me all female customers from Mumbai
```

The app will:

1. Send the query to the Groq LLM

2. Generate a SQL query

3. Execute the SQL on the customer database

4. Return and display the result

#  🛠 Troubleshooting

### 🔸 405 Method Not Allowed

- Make sure your frontend sends a POST request.
- Your backend route must use @app.post("/query").

### 🔸 CORS Error
Add CORS middleware in main.py:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 🔸 .env Not Working
Restart the server after editing .env.



