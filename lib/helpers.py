from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.all()
    for emp in employees:
        print(emp)


def find_employee_by_name():
    name = input("Enter the employee's name: ").strip()
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    try:
        id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid id")
        return

    employee = Employee.find_by_id(id)
    if employee:
        print(employee)
    else:
        print(f"Employee {id} not found")


def create_employee():
    name = input("Enter the employee's name: ").strip()
    job_title = input("Enter the employee's job title: ").strip()
    try:
        department_id = int(input("Enter the employee's department id: "))
    except ValueError:
        print("Error creating employee: department_id must be an integer")
        return

    try:
        employee = Employee(name=name, job_title=job_title, department_id=department_id)
        employee.save()
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error creating employee: {e}")


def update_employee():
    try:
        id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid id")
        return

    employee = Employee.find_by_id(id)
    if not employee:
        print(f"Employee {id} not found")
        return

    try:
        name = input("Enter the employee's new name: ").strip()
        job_title = input("Enter the employee's new job title: ").strip()
        department_id = int(input("Enter the employee's new department id: "))

        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        employee.save()
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error updating employee: {e}")


def delete_employee():
    try:
        id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid id")
        return

    employee = Employee.find_by_id(id)
    if not employee:
        print(f"Employee {id} not found")
        return

    employee.delete()
    print(f"Employee {id} deleted")


def list_department_employees():
    try:
        dept_id = int(input("Enter the department's id: "))
    except ValueError:
        print("Invalid id")
        return

    department = Department.find_by_id(dept_id)
    if not department:
        print(f"Department {dept_id} not found")
        return

    employees = department.employees()
    for emp in employees:
        print(emp)
