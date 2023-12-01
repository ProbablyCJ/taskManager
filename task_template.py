# =====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime

with open('tasks.txt', 'r') as task_data:
    tasks = ()

with open('user.txt', 'r') as user_data:
    # Variables
    user_file = user_data.readlines()
    usernames = []
    user_passwords = []


# Functions
def reg_user():
    while True:
        new_username = input("Username:   ").lower()
        new_password = input("Password:   ").lower()
        confirm_password = input("Please re-enter password:   ").lower()

        if new_password == confirm_password:
            print("New user confirmed")
            break
        else:
            print("Incorrect please try again")

    usernames.append(new_username)
    user_passwords.append(new_password)

    with open('user.txt', 'a+') as f:
        f.write(f"\n{new_username}, {new_password}")


def add_task():
    appointed_user = input("Enter appointed username:   ")
    if appointed_user not in usernames:
        print("User does not exist")
    else:

        task_title = input("Enter the tile of the task:   ")
        task_description = input("Enter task description:   ")
        date_assigned = datetime.strftime(datetime.today().date(), "%d %b %Y")
        due_date = input("Due date \n"
                         "e.g. 20 Oct 2016:     ")
        with open('tasks.txt', 'a+') as e:
            e.write(f"\n{appointed_user}, {task_title}, {task_description}, {date_assigned}, {due_date}, No")


def view_all():
    with open('tasks.txt', 'r') as m:
        file1 = m.readlines()
        for lines in file1:
            line = lines.strip().split(", ")
            line_user = line[0]
            line_date_assigned = line[3]
            line_title = line[1]
            line_description = line[2]
            line_date_due = line[4]
            line_completed = line[5]
            output = (f"\nTask:   {line_title}"
                      f"\nAssigned to:   {line_user}"
                      f"\nDate Assigned:   {line_date_assigned}"
                      f"\nDue Date:    {line_date_due}"
                      f"\nTask complete:   {line_completed}"
                      f"\nTask description: \n "
                      f"{line_description}\n")
            print(output)


def view_mine():
    with open('tasks.txt', 'r') as m:
        file1 = m.readlines()
        user_tasks = []
        all_tasks = []
        user_task_counter = 0
        for line in file1:
            line = line.strip().split(", ")

            all_tasks.append(line)
            line_user = line[0]
            if line_user == username:
                user_task_counter += 1
                user_tasks.append(line)
                line_date_assigned = line[3]
                line_title = line[1]
                line_description = line[2]
                line_date_due = line[4]
                line_completed = line[5]
                output = (f"\nTask Number: {user_task_counter}"
                          f"\nTask:   {line_title}"
                          f"\nAssigned to:   {line_user}"
                          f"\nDate Assigned:   {line_date_assigned}"
                          f"\nDue Date:    {line_date_due}"
                          f"\nTask complete:   {line_completed}"
                          f"\nTask description:  \n"
                          f"{line_description}\n")
                print(output)
            else:
                print(f"{username} has no tasks")

        user_options = int(input("Enter task number or '-1' to go to main menu: ")) - 1
        if user_options <= - 2:
            print("Going to main menu")

        else:
            if 0 <= user_options < user_task_counter:

                edited_task = True
                selected_task = user_tasks[user_options]
                selected_task_index_in_all_tasks = all_tasks.index(selected_task)

                edit_menu_option = int(input("1 - Mark As Complete\n"
                                             "2 - Change Username\n"
                                             "3 - Change Due Date\n"
                                             "Selection: "))

                if edit_menu_option == 1:
                    selected_task[-1] = "Yes"

                elif edit_menu_option == 2:
                    new_username = input("Please enter the new user's username:   ")
                    if new_username not in usernames:
                        print("User does not exist")
                    else:
                        selected_task[0] = new_username

                elif edit_menu_option == 3:
                    selected_task[-2] = input("Please enter the new due date \n"
                                              "E.g. 20 Oct 2003:   ")

                else:
                    print("Incorrect option entered, no tasks changed")
                    edited_task = False

                if edited_task:
                    all_tasks[selected_task_index_in_all_tasks] = selected_task

                    with open('tasks.txt', 'w') as write_tasks:
                        for line in all_tasks:
                            write_tasks.write(', '.join(line) + '\n')

            else:
                print("Incorrect task number entered")


def generate_report():
    with open('tasks.txt', 'r') as g_tasks:
        task_content = g_tasks.readlines()
        # Variables
        number_of_tasks = len(task_content)
        number_of_completed_tasks = 0
        number_of_incomplete_tasks = 0
        overdue_tasks = 0

        # Pulling information
        for line in task_content:
            line = line.strip().split(",")

            if line[5].lower() == 'yes':
                number_of_completed_tasks += 1
            else:
                number_of_incomplete_tasks += 1
                due_date = line[4]
                due_date = datetime.strptime(due_date.strip(), '%d %b %Y').date()
                today = datetime.today().date()
                if today > due_date:
                    overdue_tasks += 1

        overdue_percentage = (overdue_tasks / number_of_tasks) * 100
        incomplete_percentage = (number_of_incomplete_tasks / number_of_tasks) * 100

        # Creating statement format
        overview = (f"      ======== Task Overview ======== \n"
                    f"Total number of tasks   {number_of_tasks} \n"
                    f"Total number of completed tasks   {number_of_completed_tasks} \n"
                    f"Total number of incomplete tasks   {number_of_incomplete_tasks} \n"
                    f"Total number of overdue tasks   {overdue_tasks} \n"
                    f"Percentage of incomplete tasks   {incomplete_percentage}% \n"
                    f"Percentage of overdue tasks   {overdue_percentage}% \n \n")

    with open('task_overview.txt', 'w') as t:
        t.write(overview)

    print(overview)

    # Showing user overview stats
    with open('tasks.txt', 'r') as j:
        j = j.readlines()

        with open('user_overview.txt', 'w') as user_content:
            for name in usernames:
                # Variables that should reset after each loop
                user_number_of_tasks = 0
                user_task_percentage = 0
                user_overdue_percentage = 0
                user_overdue_tasks = 0
                user_incomplete_percentage = 0
                user_number_of_completed_tasks = 0
                user_number_of_incomplete_tasks = 0

                for line in j:
                    line = line.strip().split(", ")
                    if name == line[0]:
                        user_number_of_tasks += 1
                        if line[5].lower() == 'yes':
                            user_number_of_completed_tasks += 1
                        else:
                            user_number_of_incomplete_tasks += 1
                            due_date = line[4]
                            due_date = datetime.strptime(due_date.strip(), '%d %b %Y').date()
                            today = datetime.today().date()
                            if today > due_date:
                                user_overdue_tasks += 1

                # Calculations for user percentages
                try:
                    user_overdue_percentage = (user_overdue_tasks / user_number_of_tasks) * 100
                    user_incomplete_percentage = (user_number_of_incomplete_tasks / user_number_of_tasks) * 100
                    user_task_percentage = (user_number_of_tasks / number_of_tasks) * 100
                except ZeroDivisionError:
                    user_overdue_percentage = 0
                    user_incomplete_percentage = 0
                    user_task_percentage = 0

                # Creating user overview
                user_overview = (f"         =========== User Overview ========== \n"
                                 f"Registered User:         {name} \n"
                                 f"Total number of tasks assigned:   {user_number_of_tasks} \n"
                                 f"Total number of completed tasks:   {user_number_of_completed_tasks} \n"
                                 f"Total number of incomplete tasks:   {user_number_of_incomplete_tasks} \n"
                                 f"Total number of overdue tasks:   {user_overdue_tasks} \n"
                                 f"Percentage of all tasks assigned: {user_task_percentage}% \n"
                                 f"Percentage of incomplete tasks:   {user_incomplete_percentage} % \n"
                                 f"Percentage of overdue tasks:   {user_overdue_percentage} % \n \n")

                user_content.write(user_overview)
                print(user_overview)


def display_tasks():
    with open('user_overview.txt', 'r') as user_overview:
        for line in user_overview.readlines():
            print(line.strip())

    with open('task_overview.txt', 'r') as task_overview:
        print(task_overview.read())


# Loop to add information to the created variables
for i in user_file:
    line = i.strip().split(", ")
    line_username = line[0]
    line_password = line[1]

    usernames.append(line_username)
    user_passwords.append(line_password)

# ====Login Section====
while True:
    username = input("Please provide user name:   ")
    if username in usernames:
        valid_password_index = usernames.index(username)

        password = input("Please provide password:   ")
        if password == user_passwords[valid_password_index]:
            print("Welcome")
            break
        else:
            print("Incorrect Password")
    else:
        print("Incorrect username")
while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display tasks
e - Exit
: ''').lower()

    if menu == 'r' and username == 'admin':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_report()

    elif menu == 'ds':
        display_tasks()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
