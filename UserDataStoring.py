#Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and 
#emp_department and methods like calculate_emp_salary, emp_assign_department, and 
#print_employee_details. 
#Sample Employee Data: 
#"ADAMS", "E7876", 50000, "ACCOUNTING" "JONES", "E7499", 45000, "RESEARCH" "MARTIN", 
#"E7900", 50000, "SALES" "SMITH", "E7698", 55000, "OPERATIONS" 
#• Use 'assign_department' method to change the department of an employee. 
#• Use 'print_employee_details' method to print the details of an employee. 
#• Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the 
#number of hours worked by the employee. If the number of hours worked is more than 50, the 
#method computes overtime and adds it to the salary. Overtime is calculated as following formula: 
#overtime = hours_worked - 50 overtime amount = (overtime * (salary / 50))


class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id, self.emp_name, self.emp_salary, self.emp_department = emp_id, emp_name, emp_salary, emp_department

    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (salary / 50)
            total_salary = salary + overtime_amount
            return total_salary
        else:
            return salary

    def assign_department(self, new_department):
        self.emp_department = new_department
        return f"{self.emp_name}'s department has been changed to {new_department}"

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

# Get user input
emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_salary = float(input("Enter Employee Salary: $"))
emp_department = input("Enter Employee Department: ")

# Create Employee instance
employee1 = Employee(emp_id, emp_name, emp_salary, emp_department)

# Example usage with input
employee1.print_employee_details()

hours_worked = float(input("Enter hours worked: "))
new_salary = employee1.calculate_emp_salary(emp_salary, hours_worked)
print(f"New calculated salary: ${new_salary}")

new_department = input("Enter new department: ")
print(employee1.assign_department(new_department))
employee1.print_employee_details()
