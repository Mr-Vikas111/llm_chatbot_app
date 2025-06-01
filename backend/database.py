import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    """_summary_

    Returns:
        db_connect_status: return dasebase connections response
    """
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn


def execute_sql(query: str):
    """_summary_

    Args:
        query (str): take query from user input in row sql query

    Returns:
        db data: return data according to given sql query
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows