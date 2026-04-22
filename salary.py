from connection import get_connection

def add_salary():
    conn = get_connection()
    cursor = conn.cursor()

    emp_id = input("Enter employee id(For whom you're adding salary): ")
    basic_salary = float(input("Enter basic salary: "))
    allowances = float(input("Enter allowances: "))
    deductions = float(input("Enter deductions: "))

    cursor.execute("""
    INSERT INTO salary (emp_id, basic_salary, allowances, deductions)
    VALUES (%s,%s,%s,%s)""", (emp_id, basic_salary, allowances, deductions))

    conn.commit()
    cursor.close()
    conn.close()
    print("Salary added successfully!")


def view_payslip():

    conn = get_connection()
    cursor = conn.cursor()
    emp_id = input("Enter your Employee id: ")
    cursor.execute("""
    SELECT
    e.emp_id,
    e.emp_name,
    d.dept_name,
    s.basic_salary,
    s.allowances,
    s.deductions,
    s.net_salary,
    s.pay_date
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    JOIN salary s ON e.emp_id = s.emp_id
    WHERE e.emp_id = %s""", (emp_id))

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if not result:
        print("No employees found!")
    else:
        (emp_id, emp_name, dept_name, basic_salary, allowances, deductions, net_salary, pay_date) = result
        print("\n===============================")
        print("           PAYSLIP             ")
        print("===============================")
        print(f"Employee ID    : {emp_id}")
        print(f"Employee Name  : {emp_name}")
        print(f"Department     : {dept_name}")
        print(f"Date           : {pay_date}")
        print("--------------------------------")
        print(f"Basic Salary   : {basic_salary}")
        print(f"Allowances     : {allowances}")
        print(f"Deductions     : {deductions}")
        print("--------------------------------")
        print(f"Net Salary     : {net_salary}")
        print("=============================")