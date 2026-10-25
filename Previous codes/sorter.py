application_name = "Sorter Application"
options = """Options: 
1. Add data to storage 
2. list data 
3. update data 
4. delete an item 
5. list single data 
6. close application 
"""
storage = [] 
sid = 1
# this is dummy data 
movie = {"id":200,"title":"peddi","description":"crossover athelet","type":"Movie"}
file = {"id":201,"title":"peddi movie","description":"pirated file",
"link":"something.com","type":"File"}
storage.append(movie)
storage.append(file)

while True: 
    print(application_name)
    print(options)
    choice = int(input("Enter your choice ( 1 - 6 ) : "))
    match choice: 
        case 1:
            print("Adding Data: ")
            print("1. File")
            print("2. Movie")
            c = int(input("Which data you want to add (1-2): "))
            match c:
                case 1:
                    # ask for file data 
                    print("File: ")
                    title = input("Enter the Title: ")
                    desc = input("Enter the Description: ")
                    link = input("Enter the link: ")
                    file = {"id":sid,"title":title,"description":desc,"link":link,"type":"File"}
                    storage.append(file)
                    sid += 1 
                case 2:
                    # ask for movie data
                    print("Movie: ")
                    title = input("Enter the Title: ")
                    desc = input("Enter the Description: ")
                    movie = {"id":sid,"title":title,"description":desc,"type":"Movie"}
                    storage.append(movie)
                    sid += 1 
                case _ : 
                    print("Invalid choice! Try again")
                    
        case 2: 
            print("Listing all the Items: ")
            for item in storage:
                print(f"ID: {item["id"]}")
                print(f"Title: {item["title"]}")
                print(f"Type: {item["type"]}")
                print() # one line gap 
        case 3: 
            print("Updating Data: ")
        case 4:
            print("Deleting an Item: ")
        case 5: 
            print("List Single Data: ")
        case 6:
            print("Closing application...")
            break 
    approval = input("Do you wish to continue (y/n) : ")
    if approval.lower() == "y":
        continue 
    else:
        print("Closing application....")
        print("Thank you...")
        break 
