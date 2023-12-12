global tasks
tasks=[]
def add_tasks():
    loop_status = True
    while True:
        #Taking the Input from the user....
        Task=input("Enter the Task of the Task:")
        Priority=input("Enter the Priority of the Task:")
        Duedate=input("Enter the Duedate of the Task:")
        #Status=input("Enter the status of the Task:")
        #Add the task details to the tasks lists as a dictionary format....
        in_dict={"Task":Task,"Priority":Priority,"Duedate":Duedate,"Status":"Not completed"}
        tasks.append(in_dict)
        choice=input("Do you want to add new task again[Yes/No]")
        if choice.upper()=='No':
            loop_status = False
        print(tasks, end="\n") 
        print("Add tasks")  
add_tasks()

tasks={}
def update_tasks():
    loop_status = True
    while True:
        #Taking the Input from the user....
        Task=input("Enter the Task of the Task:")
        Priority=input("Enter the Priority of the Task:")
        Duedate=input("Enter the Duedate of the Task:")
        #Status=input("Enter the status of the Task:")
        #Add the task details to the tasks lists as a dictionary format....
        in_dict={"Task":Task,"Priority":Priority,"Duedate":Duedate,"Status":"Not completed"}
        tasks.update(in_dict)
        choice=input("Do you want to add new task again[Yes/No]")
        if choice.lower()=='No':
            loop_status = False
        print(tasks, end="\n") 
        print("Update tasks")  
update_tasks()

tasks=[]
def display_tasks():
    loop_status = True
    while True:
        #Taking the Input from the user....
        Task=input("Enter the Task of the Task:")
        Priority=input("Enter the Priority of the Task:")
        Duedate=input("Enter the Duedate of the Task:")
        #Status=input("Enter the status of the Task:")
        #Add the task details to the tasks lists as a dictionary format....
        in_dict={"Task":Task,"Priority":Priority,"Duedate":Duedate,"Status":"Not completed"}
        print(in_dict)
          
display_tasks()
