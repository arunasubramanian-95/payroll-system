import psycopg2
from connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            dept_id     SERIAL PRIMARY KEY,
            dept_name   VARCHAR(100) NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id      SERIAL PRIMARY KEY,
            emp_name    VARCHAR(100) NOT NULL,
            email       VARCHAR(100) NOT NULL UNIQUE,
            phone       VARCHAR(15),
            dept_id     INT REFERENCES departments(dept_id),
            role        VARCHAR(20) NOT NULL,
            join_date   DATE DEFAULT CURRENT_DATE,
            city        VARCHAR(20) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS salary (
            salary_id       SERIAL PRIMARY KEY,
            emp_id          INT REFERENCES employees(emp_id),
            basic_salary    NUMERIC(10,2) NOT NULL,
            allowances      NUMERIC(10,2) DEFAULT 0,
            deductions      NUMERIC(10,2) DEFAULT 0,
            net_salary      NUMERIC(10,2) GENERATED ALWAYS AS 
                            (basic_salary + allowances - deductions) STORED,
            pay_date        DATE DEFAULT CURRENT_DATE
        )
    """)
    cursor.execute("""
        INSERT INTO departments(dept_name)
        VALUES('IT')
        ON CONFLICT (dept_name) DO NOTHING""")
    cursor.execute("""
        INSERT INTO employees (emp_name, email, phone, dept_id, role, city)
        VALUES('Radha Krishnan', 'radha.krishnan@gmail.com', '8796541235', 1, 'Admin', 'Bengaluru')""")

    conn.commit()
    cursor.close()
    conn.close()
    print("All tables created successfully!")

if __name__ == "__main__":
    setup_database()