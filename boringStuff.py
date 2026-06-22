'''
Boring stuff: 
1. Cleaning 
2. Studying 
3. Listening to Lecture 

1. Adding the task 
taskID: # generate it automatically 
task Name: 
task Description: 
author: 
pay: 
is_completed: # by default set to False 

2. Picking the task : 
Enter the task ID: 

Task is completed sucessfully 

Task not found , Try again 

3. Displaying the task: 
Enter ther task ID: 

ID : 
Title: 
Description: 
Author: 
Pay: 
Is completed: 

4. Displaying all the available tasks: 

Taks: 
ID: 
Title: 
Description: 

ID: 
Title: 
Description: 

'''

tasks = [
    {
        "taskID": 1,
        "task Name": "Cleaning",
        "task Description": "",
        "user_id": 1,
        "pay": 10,
        "is_completed": False
    },
    {
        "taskID": 2,
        "task Name": "Studying",
        "task Description": "",
        "user_id": 2,
        "pay": 20,
        "is_completed": False
    },
    {
        "taskID": 3,
        "task Name": "Listening to Lecture",
        "task Description": "",
        "user_id": 3,
        "pay": 30,
        "is_completed": False
    }
]

users = [
{
    "id":1,
    "name":"Alekhya",
    "balance": 100
},
{
    "id":2,
    "name":"Srilekhya",
    "balance": 100
},
{
    "id":3,
    "name":"Sharukh",
    "balance": 100
}
]

all_ids = [1,2,3]
next_id = 4
user_id = 4 

while True:
    print("\n1. Adding the task")
    print("2. Picking the task :")
    print("3. Displaying the task:")
    print("4. Displaying all the available tasks:")
    print("5. Create an account")
    print("6. List all accounts")
    print("7. Check Account Balance")
    print("8. Exit")
    
    choice = input("\nEnter choice: ").strip()
    
    match choice:
        case '1':
            print("Creating a Task: ")
            print(f"taskID: {next_id}")
            name = input("task Name: ")
            desc = input("task Description: ")
            uid = int(input("user ID: "))
            pay = (int(input("pay: ")))
            
            new_task = {
                "taskID": next_id,
                "task Name": name,
                "task Description": desc,
                "user_id": uid,
                "pay": pay,
                "is_completed": False
            }
            tasks.append(new_task)
            all_ids.append(next_id)
            next_id += 1
        case '2':
            print("Mark Task as completed: ")
            search_id = int(input("Enter the task ID: "))
            cid = int(input("Enter Your user ID: "))
            
            if search_id in all_ids:
                for task in tasks:
                    if task["taskID"] == search_id:
                        uid = task["user_id"]
                        user = {}
                        cuser = {}
                        for u in users:
                            if u["id"] == uid:
                                user = u 
                                break 
                        for u in users:
                            if u["id"] == cid:
                                cuser = u 
                                break 
                        if task["pay"] <= user["balance"]:
                            task["is_completed"] = True
                            # to transfer the funds 
                            pay = task["pay"]
                            user["balance"] = user["balance"] - pay 
                            cuser["balance"] = cuser["balance"] + pay 
                            print("Task is completed sucessfully")
                        else:
                            print("Task is not completed because of Insufficient Funds")
            else:
                print("Task not found , Try again")
                
        case '3': # searching for task 
            print("Task Details:")
            search_id = int(input("Enter ther task ID: "))
                
            if search_id in all_ids:
                for task in tasks:
                    if task["taskID"] == search_id:
                        print(f"ID : {task['taskID']}")
                        print(f"Title: {task['task Name']}")
                        print(f"Description: {task['task Description']}")
                        print(f"User ID: {task['user_id']}")
                        print(f"Pay: {task['pay']}")
                        print(f"Is completed: {task['is_completed']}")
                        break 
            else:
                print("Task not found , Try again")
                
        case '4': # all the available tasks 
            print("All available Tasks:")
            for task in tasks:
                print(f"ID: {task['taskID']}")
                print(f"Title: {task['task Name']}")
                print(f"Description: {task['task Description']}")
                print()
                
        case '5':
            # username -> dictonary {id,name} => users 
            print("Creating account:")
            username = input("Enter your name: ")
            user = {"id":user_id,"name":username,"balance":100}
            users.append(user)
            user_id += 1 
            print("User Created Sucessfully...")
            
        case '6':
            print("Displaying accounts:")
            for user in users: 
                print(f"ID: {user["id"]}")
                print(f"Name: {user["name"]}")
                print()
        case '7':
            search_id = int(input("Enter your user ID: "))
            user = {}
            for u in users:
                if u["id"] == search_id:
                    user = u 
                    break 
            print(f"Balance: {user["balance"]}")
        case '8':
            print("Exiting the application....")
            break 
        case _ :
            print("Invalid choice, Try again.")
            
    
