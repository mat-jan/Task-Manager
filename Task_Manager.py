import json
import os
import sys

def main():
    json_data = []
    if os.path.exists("task_list.json"):
        try:
            with open("task_list.json", "r") as j:
                loaded_data = json.load(j)
                
            if isinstance(loaded_data, list):
                json_data = loaded_data
            else:
                print("Warning: File data.json contains invalid data format. Initializing an empty task list.")
                
        except json.JSONDecodeError:
            print("Warning: File data.json contains invalid data format. Initializing an empty task list.")
    else:
        with open("task_list.json", "w") as j:
            json.dump([], j, indent=2)
    print("File 'task_list.json' not found, created new empty JSON file.")       
            
    what_want_ask = input("Add new task (1), Show my tasks (2), Delete tasks(3): ")
    next_id = 1 
    if what_want_ask in ["1"]:
        if json_data == []:
            next_id=1
        else:
            max_id = max(json_data, key=lambda zadanie: zadanie["ID"])["ID"]
            next_id = max_id +1
        user(json_data,next_id)    
    elif what_want_ask in ["2"]:
        show_tasks(json_data)
    elif what_want_ask in ["3"]:
        delete_tasks(json_data)
    else:
        print("Type correct!!!")
        main()
    
    
def user(json_data,next_id):
    status=""
    priority=""
    title_ask = input("Name task: ")
    status_ask = input("Set task status (1) undone, (2) done: ")
    while status_ask not in ["1","2"]:
        status_ask = input("Set task status (1) undone, (2) done: ")
    else:
        if status_ask == "1":
            status = "undone"
        elif status_ask == "2":
            status = "done"
        else:
            print("You don't name taks!")
    priority_ask = input("Set task priority (1) High, (2)Averge, (3)Low: ")
    while priority_ask not in ["1","2","3"]:
        priority_ask = input("Set task priority (1) High, (2)Averge, (3)Low: ")
    else:    
        if priority_ask == "1":
            priority = "high"
        elif priority_ask == "2":
            priority = "averge"
        elif priority_ask == "3":
            priority = "low"    

    zadanie = {"ID":next_id, "Title":title_ask, "Status":status, "Prioryty":priority}
    json_data.append(zadanie)
    with open ("task_list.json", "w") as j:
        json.dump(json_data, j , indent=2)
    print(f"Added {zadanie} to yout task list! ")
    ask_for_restart()
        


    
def show_tasks(json_data):
    for zadanie in json_data:
        print(f"ID: {zadanie["ID"]} | Title: {zadanie['Title']} | Status: {zadanie['Status']} | Prioryty: {zadanie['Prioryty']}")
    if json_data == []:
        print("List is clear.")
    ask_for_restart() 
        
def delete_tasks(json_data):
    for zadanie in json_data:
        print(f"ID: {zadanie['ID']} | Title: {zadanie['Title']} | Status: {zadanie['Status']} | Prioryty: {zadanie['Prioryty']}")
    ask_for_delete = input("Which taks you want to delete type (if no one type exit): ")
    if ask_for_delete.lower() in ["exit"]:
        ask_for_restart()
    ids = [z["ID"] for z in json_data]
    while ask_for_delete.isdigit() not in ids:
        print("Type correct ID")
        ask_for_delete = input(ask_for_delete)
    else:
        json_data=[zadanie for zadanie in json_data if zadanie["ID"] != ask_for_delete]
    for i, zadanie in enumerate(json_data, start=1):
        zadanie["ID"] = i
    with open ("task_list.json", "w") as j:
        json.dump(json_data, j , indent=2)
    print(f"Delete {zadanie['Title']} from your task list! ")
    ask_for_restart()

def ask_for_restart():
    ask_for_restart = input("Do you want to go to main? (yes/no) ")
    while ask_for_restart.lower() in ["yes","y","no","n"]:
        if ask_for_restart.lower() in ["yes", "y"]:
            print("Okey going to main...")
            main()
        else:
            exit_program()
    else:
        ask_for_restart = input("Do you want to go to main? (yes/no) ")
        
def exit_program():
    print("Okey you exited program.")
    sys.exit()

main()