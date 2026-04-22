import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="payroll_system",
        user="postgres",
        password="SQL" 
    )
    return connection

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")