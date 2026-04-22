from connection import get_connection

def add_employee():
    conn = get_connection()
    cursor = conn.cursor()

    emp_name = input("Please enter employee name: ")
    email = input("Please enter employee email address: ")
    phone = input("Please enter employee phone number: ")
    role = input("Please enter employee role: ")
    dept_name = input("Please enter department name: ")
    city = input("Please enter your city name: ")
    cursor.execute("""
    INSERT INTO departments (dept_name)
    VALUES (%s)
    ON CONFLICT (dept_name) DO NOTHING
""", (dept_name,))
    cursor.execute("""
    SELECT dept_id FROM departments WHERE dept_name = %s""", (dept_name,))
    result = cursor.fetchone()
    dept_id = result[0]

    cursor.execute("""
    INSERT INTO employees (emp_name, email, phone, role, dept_id, city)
    VALUES(%s, %s, %s, %s, %s, %s)""", (emp_name, email, phone, role, dept_id, city))

    conn.commit()
    cursor.close()
    conn.close()
    print("Employee added successfully!")

def view_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT
        e.emp_id,
        e.emp_name,
        e.email,
        e.phone,
        e.role,
        d.dept_name AS Department,
        e.join_date AS Joining_date
        FROM employees e
        LEFT JOIN departments d
        ON e.dept_id = d.dept_id
        ORDER BY e.emp_id ASC""")

        result = cursor.fetchall()

        if not result:
            print("No employees found!")
        else:
            print("\n" + "=" * 120)
            print("                                             EMPLOYEES LIST                                                ")
            print("=" * 120)
            print("Employee ID  |Employee Name  |       Email              |    Phone   |       Role       |    Department    |Join Date")
            print("=" * 120)
            for row in result:
                print(f"{row[0]:<13}|{row[1]:<15}|{row[2]:<26}|{row[3]:<12}|{row[4]:<18}|{row[5]:<18}|{row[6]}")
            print("=" * 120)
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()