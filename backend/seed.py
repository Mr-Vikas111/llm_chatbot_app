from database import get_db

def seed():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS customers;")
    cursor.execute("""
        CREATE TABLE customers (
            customer_id SERIAL PRIMARY KEY,
            name TEXT,
            gender TEXT,
            location TEXT
        );
    """)
    
    cursor.executemany(
        "INSERT INTO customers (name, gender, location) VALUES (%s, %s, %s);",
        [
            ("Vikash", "Male", "Mumbai"),
            ("Rohit", "Male", "Delhi"),
            ("Megha", "Female", "Mumbai"),
            ("Rahul", "Male", "Chennai"),
            ("Ruhi", "Female", "Pune"),
        ]
    )
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    seed()