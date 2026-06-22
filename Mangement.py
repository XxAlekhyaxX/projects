import random 
application_name = "Employee Management System"
options="""Options:
1. Create an Employee
2. Display Employee Details 
3. Credit Salary for Employee
4. Mark Attendance for Employee
5. Generate Index 
"""
employees = []
employee_index = {}
roles = ("Manager","Developer","Assistant Developer","Tester")
salaries = (40000,70000,50000,55000)
num_roles = len(roles)
eid = 1 
while True:
    print(application_name)
    print(options)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Creating Employee Account: ")
            name = input("Enter Name: ")
            joining_date = input("Enter joining date (dd/mm/yyyy): ")
            index = random.randint(1,num_roles)
            employee = {"id":eid,"name":name,"salary":salaries[index],
                        "role":roles[index],"joining_date":joining_date}
            employees.append(employee)
            eid = eid + 1 
        case 2:
            target = int(input("Enter the Employee ID: "))
            index  = employee_index.get(target)
            if index == None: 
                print("Employee not found")
            else:
                employee = employees[index]
                print(f"ID: {employee["id"]}")
                print(f"Name: {employee["name"]}")
                print(f"Role: {employee["role"]}")
                print(f"Salary: {employee["salary"]}")
                print(f"Joining Date: {employee["joining_date"]}")
        case 5:
            for i in range(len(employees)):
                employee = employees[i]
                employee_index[employee["id"]] = i 
                
        case _:
            print("Still not Implemented")
    
