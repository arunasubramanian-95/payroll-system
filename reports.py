from connection import get_connection

def department_report():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT
        d.dept_name,
        COUNT(e.emp_id) AS employees,
        AVG(s.net_salary) AS avg_salary
        FROM departments d
        LEFT JOIN employees e
        ON d.dept_id = e.dept_id
        LEFT JOIN salary s
        ON e.emp_id = s.emp_id
        GROUP BY d.dept_name
        ORDER BY d.dept_name ASC""")

        result = cursor.fetchall()
        if not result:
            print("No reports found!")
            return

        print("=" * 47)
        print("|     Department     | Employees | Avg Salary |")
        print("=" * 47)
        for row in result:
            print(f"| {row[0]:<17}  | {row[1]:^8}  | {row[2]:>6.2f}   |")
        print("=" * 47)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()

def top_earners():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT
        e.emp_id AS Employee_ID,
        e.emp_name AS Employee_Name,
        s.net_salary AS salary,
        d.dept_name AS Department_Name,
        rank() OVER(ORDER BY s.net_salary DESC) AS Ranked_salary
        FROM employees e
        LEFT JOIN departments d
        ON e.dept_id = d.dept_id
        LEFT JOIN salary s
        ON e.emp_id = s.emp_id
        LIMIT 3""")

        result = cursor.fetchall()
        if not result:
            print("No reports found!")
            return

        print("Employee ID  |  Employee Name  |  Salary  |  Department_Name  |  Highest Earners Rank")
        print("-" * 25)
        for row in result:
            print(f"{row[0]:>5}  | {row[1]:>12}  |  {row[2]:>14}  |  {row[3]:>12}  |  {row[4]:2f}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()