from fastapi import FastAPI, HTTPException
from database import get_db, execute_sql
from groq_setup import generate_sql_query
import logging
from fastapi.middleware.cors import CORSMiddleware

# import basemodel schemas
from model_schemas import QueryRequest


# initialize fast api app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def query_process(req: QueryRequest):
    try:
        sql_query = await generate_sql_query(req.user_query)
        results = execute_sql(sql_query)
        return {"sql": sql_query, "results": results}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong.")

