students = []
tasks = []

while True:
    print("\n1. Create Student")
    print("2. Add Task")
    print("3. Display all tasks for a student")
    print("4. Display single task")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("\nCreating Student Account:")
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        school = input("Enter School: ")
        
        sid = len(students) + 1
        student = {
            "id": sid,
            "name": name,
            "grade": grade,
            "school": school
        }
        students.append(student)
        print("Success: Created Student with ID", sid)
        
    elif choice == 2:
        print("\nAdding a Task:")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        priority = input("Enter Priority (low/medium/high): ")
        student_id = int(input("Enter Student ID Number: "))
        
        student_exists = False
        for i in range(len(students)):
            if students[i]["id"] == student_id:
                student_exists = True
                
        if student_exists:
            tid = len(tasks) + 1
            task = {
                "id": tid,
                "title": title,
                "description": description,
                "priority": priority,
                "student_id": student_id,
                "status": False
            }
            tasks.append(task)
            print("Success: Added Task with ID", tid)
        else:
            print("Error: Student ID does not exist.")
            
    elif choice == 3:
        search_id = int(input("\nEnter the student ID Number: "))
        print("\n--- Tasks ---")
        found_any = False
        for i in range(len(tasks)):
            task = tasks[i]
            if task["student_id"] == search_id:
                status_text = "Completed" if task["status"] else "Pending"
                print("ID:", task["id"], "| Title:", task["title"], f"[{status_text}]")
                found_any = True
        if not found_any:
            print("No tasks found for this student.")
            
    elif choice == 4:
        search_id = int(input("\nEnter the task ID Number: "))
        found = False
        for i in range(len(tasks)):
            task = tasks[i]
            if task["id"] == search_id:
                print("\n--- Task Details ---")
                print("ID:", task["id"])
                print("Title:", task["title"])
                print("Description:", task["description"])
                print("Priority:", task["priority"])
                print("Student ID:", task["student_id"])
                print("Status:", "Completed" if task["status"] else "Pending")
                found = True
                
                if not task["status"]:
                    change = input("Mark this task as Completed? (yes/no): ")
                    if change.lower() == "yes":
                        task["status"] = True
                        print("Success: Task status updated to Completed.")
                        
        if not found:
            print("Task is not found.")
            
    elif choice == 5:
        print("\nExiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
