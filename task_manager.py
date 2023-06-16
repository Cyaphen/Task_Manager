'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
from cgi import print_environ
from datetime import date
from collections import Counter
from msilib.schema import AdminExecuteSequence

# Opening files
data = open('user.txt', 'r')
work = open('tasks.txt', 'r')
task = open('task_overview.txt', 'w')
user = open('user_overview.txt', 'w')
current_day = date.today()

# Function to register a new user, creating password and username lists for access and login
def reg_user():
    repeat = True
    data = open('user.txt', 'r')
    for line in data:
        data = open('user.txt', 'r')
        line = line.strip().split(", ")
        b = line[1]
        username_list.append(line[0])
        password_list.append(b)
        while repeat:                           # Loop for the user to continue input if entry is wrong
            print()
            username = input("Enter username:")
            password = input("Enter password:")
            if username != username_list[0]:
                print("You don't have acces to register a new user.")
            elif password != password_list[0]:
                print("Password doesn't match, retry.")
            else:
                if username == username_list[0] and password == password_list[0]:
                    print("Acces granted.") 
                    print()
                    data = open('user.txt', 'r+')
                    for line in data:
                        data = open('user.txt', 'r+')
                        line = line.strip().split(', ')
                        b = line[1]
                        username_list.append(line[0])
                        password_list.append(b)
                        while repeat:
                            new_user = input("Enter new username:")
                            new_pass = input("Enter new password:")
                            new_pass1 = input("Confirm password:")
                            if new_pass != new_pass1:
                                print("passwords don't match, retry.")
                            if new_user in username_list:
                                print("Username already exists, retry.")
                            if new_pass1 in password_list:
                                print("Password already exists, retry.")
                            else:
                                if new_user not in username_list and new_pass == new_pass1:
                                    data = open('user.txt', 'a')
                                    data.write(new_user + ", " + new_pass1 + "\n")
                                    print()
                                    data.close()
                                    repeat = False
    return("Registration succesful.")

# Adding a task to user
def add_task():
    work = open('tasks.txt', 'r')
    print()
    user_task = input("Enter the username to whom the task is assigned to: ")
    title_task = input("Enter the title of the task: ")
    info_task = input("Enter the description of the task at hand: ")
    current_day = date.today()
    due_date = input("Enter the date by when the task must be completed in the following format('2022-08-14): ")
    complete_task = ("No")
    print()
    work = open('tasks.txt', 'a')
    work.write(user_task + ", " + title_task + ", " + info_task + ", " + str(current_day) + ", " + due_date + ", " + complete_task + "\n")
    print()
    work.close()
    return("Task created succesfully.")
# Show all tasks created and stored in tasks.txt, count set up to show task number  
def view_all():
    work = open('tasks.txt', 'r')
    count = 0
    for line in work:
        work = open('tasks.txt', 'r')
        count += 1
        line= line.strip().split(', ')
        edit_user = line[0]
        edit_date = line[4]
        edit_complete = line[5]
        print("Task "+str(count)+":\t\t\t" + line[1])
        print("Assigned to:\t\t" + edit_user)
        print("Date assigned:\t\t" + line[3])
        print("Due date:\t\t" + edit_date)
        print("Task complete:\t\t" + edit_complete)
        print("Task description:\n" +line[2])
        print()
    return("All tasks displayed successfuly.")
# Code to show user specific tasks only
def view_mine():
    work = open('tasks.txt', 'r')
    count = 0
    for line in work:
        work = open('tasks.txt', 'r')
        count = count + 1
        line = line.strip().split(', ')
        if username == line[0]:
            edit_user = line[0]
            edit_date = line[4]
            edit_complete = line[5]
            print("Task "+str(count)+":\t\t\t" + line[1])
            print("Assigned to:\t\t" +edit_user)
            print("Date assigned:\t\t" +line[3])
            print("Due date:\t\t" +edit_date)
            print("Task complete:\t\t" +edit_complete)
            print("Task description:\n" +line[2])
            print()
    return("Users tasks displayed successfuly")
# Extra function to display tasks to user
def task_format():
    work = open('tasks.txt', 'r')
    count = 0
    for line in work:
        count += 1
        line = line.strip().split(', ')
        if line[-1] == 'No':
            edit_user = line[0]
            edit_date = line[4]
            edit_complete = line[5]
            description = ('Task '+str(count)+': '+line[1] +'\nAssigned to: '+edit_user+ '\nDue date: '+edit_date+ '\nTask complete: '+edit_complete)
            print(description)
            print()
    return('Tasks displayed successfuly')

#   ====Login Section====
# Setting up loops to verify users and grant access
# Statements that check if the password belongs to that user and other way around 

username_list = []
password_list = []
repeat = True
data = open('user.txt', 'r')
succesful_login = False     # Assisted by Logan
while(True):
    print("Welcome, please log in to continue.")
    username = input("Enter username:")
    password = input("Enter password:")
    print()
    for line in data:
        data = open('user.txt', 'r')
        line = line.strip().split(', ')
        username_list.append(line[0])
        password_list.append(line[1])
        print()
        if username in username_list and password in password_list:
            print("Login succesful.")
            print("Welcome, " + username)
            data.close()
            succesful_login = True
            break
    if succesful_login == True:
        break
    else:
        print('username or password incorrect')        

# Loops through menu and selections until exit is selected       
while True:
            print()
            menu = input('''Select one of the following Options below:
                    r - Register user
                    a - Adding a task
                    va - View all tasks
                    vm - view my task
                    gr - Generate reports
                    ds - Display statistics
                    e - Exit
                    : ''').lower()
# Code to register new user with only admin access granted to do so.
            if menu == 'r':
                print()
                print(reg_user())                                                   
                                    
# Code for user to add tasks and writes to task file.                                                    
            elif menu == 'a':
                print()
                print(add_task())
                
# User can view all tasks assigned to all users, dsplayed as in 'output 2'                        
            elif menu == 'va':
                print()
                work = open('tasks.txt', 'r')
                print(view_all())
                work.close()

# User to view their task only with options to edit
            elif menu == 'vm':
                print()
                menu_choice = 0
                data = open('user.txt', 'r')
                work = open('tasks.txt', 'r')
                while menu_choice != -1:
                    menu_choice = int(input('''Choose one of the following numbers below:
                                        1 - View tasks
                                        2 - Mark tasks complete
                                        3 - Edit tasks
                                        -1 - Return to menu
                                        :'''))
                    if menu_choice == 1:
                        print()
                        print(view_mine())
                    elif menu_choice == 2:
                        task_list = []
                        while menu_choice != -1:
                            for line in work:
                                work = open('tasks.txt', 'r+')
                                line = line.strip().split(', ')
                                if username == line[0]:
                                    task_list.append(line)
                                for index, title in enumerate(task_list, start = 0):
                                    edit_list = index + 1, title[1]
                                    print()
                                menu_choice = int(input('''Choose one of the following options below:
                                                            1 - Mark task as complete
                                                            -1 - Exit to menu
                                                            :'''))
                                if menu_choice == -1:
                                    break
                                print(edit_list)
                                print("Type 'yes' to mark task complete, 'no' if task is incomplete and 'zero' to exit.")
                                this = input('Mark this task complete? ').lower()
                                if (menu_choice  == 1) and (this == 'yes'):
                                    title[-1] = 'Yes'
                                    work = open('tasks.txt', 'a')
                                    work.write(str(title).replace('[', '').replace(']', '').replace("'", "", 12)+'\n')
                                    print('Task marked complete.')
                                if this == 'no':
                                    print('Returning to menu.')
                                if this == 'zero':
                                    break                            
                                                                                            
                    elif menu_choice == 3:
                        edit_tasks = []
                        edit_complete = []
                        for line in work:
                            work = open('tasks.txt', 'r')
                            line = line.strip().split(', ')
                            if line[-1] == 'No':
                                edit_complete.append(line[-1])
                                edit_tasks.append(line)
                                for index,title in enumerate(edit_tasks, start = 0):  # Finding index and charachter value
                                    task_titles = index + 1, title[1]
                            while menu_choice != -1:
                                menu_choice = int(input('''Choose one of the following options below:
                                            1 - Change username of the task
                                            2 - Change due date of the task
                                            -1 - Exit menu
                                            :'''))
                                if menu_choice == 1:
                                    print(task_format())
                                    enter = int(input('Enter the task number you wish to change the username for: '))
                                    if enter <= len(edit_tasks): # range set up for total number of tasks
                                        edit_username = input('Enter username: ')
                                        title[0] = edit_username
                                        work = open('tasks.txt', 'a')
                                        work.write(str(title).replace('[', '').replace(']', '').replace("'", "", 12)+'\n')
                                    else:
                                        print('Incorrect selection, returning to menu.')
                                if menu_choice == 2:
                                    print(task_format())
                                    enter = int(input('Enter the task number you want to change the due date of the task: '))
                                    if enter <= len(edit_tasks):
                                        print('Enter the date in the following format: "10 Aug 2022"')
                                        edit_date = input('Enter the new due date of the task: ')
                                        title[4] = edit_date
                                        work = open('tasks.txt', 'a')
                                        work.write(str(title).replace('[', '').replace(']', '').replace("'", "", 12))
                                        work.write('\n')
                                    else:
                                        print('Incorrect selection, returning to menu')
                print()                
                work.close()
                
            elif menu == 'gr':
                data = open('user.txt', 'r')
                work = open('tasks.txt', 'r')
                number_tasks = len(work.readlines())
                task = open('task_overview.txt', 'a')
                task.write('Number of tasks generated: '+str(number_tasks)+'\n')
                no_tasks = []
                yes_tasks = []
                work = open('tasks.txt', 'r')
                for line in work:
                    work = open('tasks.txt', 'r')
                    line = line.strip().split(', ')
                    if line[-1] == 'No':
                        no_tasks.append(line[-1])    
                    if line[-1] == 'Yes':
                        yes_tasks.append(line[-1])
                no_count = len(no_tasks)
                yes_count = len(yes_tasks)
                task = open('task_overview.txt', 'a')
                task.write('Total number of completed tasks: '+str(yes_count)+'\n')
                task.write('Total number of uncompleted task: '+str(no_count)+'\n')
                overdue = 0 
                current_day = str(date.today())
                current_day = current_day.replace('-', '') # Removing unwanted charachters from date
                current_day = int(current_day) # Cast to integer for calcualtion purposes
                for line in work:
                    line = line.strip().split(', ')
                    line[4] = line[4].replace('-', '')
                    date_incomplete = line[4]
                if (line[-1] == 'No') and int(date_incomplete) < current_day: # Finding incomplete and overdue tasks
                        overdue +=1
                task.write('Total number of overdue tasks are: '+str(overdue)+'\n')
                per_incomp = ((no_count/number_tasks)*100)  # Calculations and rounding of answers
                per_incomp = round(per_incomp, 2)
                per_overdue = ((overdue/number_tasks)*100)
                per_overdue = round(per_overdue, 2)
                task.write('The percantage of tasks that are incomplete is: '+str(per_incomp)+'%\n')
                task.write('The percantage of tasks that are overdue is: '+str(per_overdue)+'%\n')
                task.close()
                user.close()
                work.close()
                data.close()
            
            elif menu == 'ds':
                user = open('user_overview.txt', 'a')
                print()
                repeat = True
                data = open('user.txt', 'r')
                for line in data:
                    data = open('user.txt', 'r')
                    line = line.split(", ")
                    b = line[1].strip()
                    username_list.append(line[0])
                    password_list.append(b)
                    while repeat:                           # Loop for the user to continue input if entry is wrong
                        print()
                        username = input("Enter username:")
                        password = input("Enter password:")
                        if username != username_list[0]:
                            print("You don't have acces to view statistics.")
                        elif password != password_list[0]:
                            print("Password doesn't match, retry.")
                        else:
                            if username == username_list[0] and password == password_list[0]:
                                print()
                                print("Acces granted, reports have been generated in file")
                                repeat = False
                data = open('user.txt', 'r')
                users = len(data.readlines())
                work = open('tasks.txt', 'r')
                duties = len(work.readlines())
                user.write('Total number of users: '+str(users)+'\n')  # Write to file
                user.write('Total number of tasks: '+str(duties)+'\n')
                work = open('tasks.txt', 'r')
                reg_users = []
                yes_task = []
                no_task = []
                current_day = str(date.today())
                current_day = current_day.replace('-', '')
                current_day = int(current_day)
                overdue = 0
                for line in work:
                    line = line.strip().split(', ')
                    name = line[0]
                    line[4] = line[4].replace('-', '')
                    date_incomplete = line[4]
                    reg_users.append(name)                    
                    user_dictionary = Counter(reg_users) # Counting user tasks, putting in dictionary
                    if line[-1] == 'No':
                        no_task = line[-1]
                    if line[-1] == 'Yes':
                        yes_task = line[-1]
                    if (line[-1] == 'No') and int(date_incomplete) < current_day:
                        overdue += 1
                yes_task = len(yes_task)
                no_task = len(no_task)        
                for key, value in user_dictionary.items():  # Setting up for loop to get each users information
                    user.write('Username: '+str(key)+'\n')
                    user.write('Total number of tasks: '+str(value)+'\n')
                    value = str(value)
                    value = int(value)
                    perc_assigned = (value/duties) * 100  # Calculations and rounding
                    perc_assigned = round(perc_assigned, 2)
                    user.write('Percantage of tasks assigned: '+str(perc_assigned)+'%\n')                  
                    perc_compl = (yes_task/duties) * 100
                    perc_compl = round(perc_compl, 2)
                    perc_incompl = (no_task/duties) * 100
                    perc_incompl = round(perc_incompl, 2)
                    user.write('Percantage of completed tasks: '+str(perc_compl)+'%\n')
                    user.write('Percantage of incomplete tasks: '+str(perc_incompl)+'%\n')
                    perc_overdue = (overdue/duties) * 100
                    perc_overdue = round(perc_overdue, 2)
                    user.write('Percantage of tasks incomplete and overdue: '+str(perc_overdue)+'%\n')
                user.close()
                data.close()
                work.close()
                task.close() 

            elif menu == 'e':
                data.close()    # Closing opened files
                work.close()
                task.close()
                user.close()
                print('Goodbye!!!')
                exit()
            else:
                print("You have made a wrong choice, Please Try again")

# https://www.youtube.com/watch?v=fptTG4OF4f4&t=213s
# https://stackoverflow.com/questions/67819970/python-connecting-scartted-information-that-belongs-to-the-same-person