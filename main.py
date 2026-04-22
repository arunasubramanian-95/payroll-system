from connection import get_connection
from employees import add_employee, view_all_employees
from salary import add_salary, view_payslip
from reports import department_report, top_earners

def main_menu():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        emp_id = input("Enter Employee ID: ")

        while True:
            cursor.execute("SELECT role, emp_name FROM employees WHERE emp_id = %s", (emp_id,))
            result = cursor.fetchone()

            if result:
                user_role = result[0]
                emp_name = result[1]
                print(f"Hello {emp_name}")
                break

            print(f"Employee ID {emp_id} not found.")
            emp_id = input("Please enter a valid Employee ID: ")

        while True:
            if result:
                print("\n" + "=" * 27)
                print("  EMPLOYEE PAYROLL SYSTEM   ")
                print("=" * 27)
                print("1. View All Employees")
                print("2. View Payslip")

                if user_role == "Admin":
                    print("3. Add Employee")

                elif user_role == "HR":
                    print("3. Add Salary")

                elif user_role == "Manager":
                    print("3. Department Report")
                    print("4. Top Earners Report")

                print("0. Exit")
                print("=" * 27)
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    view_all_employees()
                elif choice == 2:
                    view_payslip()
                elif choice == 3:
                    if user_role == "Admin":
                        add_employee()
                    elif user_role == "HR":
                        add_salary()
                    elif user_role == "Manager":
                        department_report()
                elif choice == 4 and user_role == "Manager":
                    top_earners()
                elif choice == 0:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice! Please try again.")
    except Exception as e:
        print(f"Invalid Input {e}")
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    main_menu()