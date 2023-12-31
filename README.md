# Task_Manager

This program works with two text files, user.txt and tasks.txt.

The file tasks.txt stores a list of all the tasks that the team is working on.
Note that this text file already contains data about two tasks. The data for
each task is stored on a separate line in the text file. Each line
includes the following data about a task in this order:

* The username of the person to whom the task is assigned.
* The title of the task.
* A description of the task.
* The date that the task was assigned to the user.
* The due date for the task.
* Either a ‘Yes’ or ‘No’ value that specifies if the task has been
completed yet.

The file user.txt stores the username and password for each user that has
permission to use the program (task_manager.py).
Note that this text file already contains one default user that has the username, ‘admin’
and the password, ‘adm1n’. The username and password for each
user gets written to this file in the following format:

* First, the username followed by a comma, a space and then
the password.
* One username and corresponding password per line

Only the user with the username ‘admin’ is allowed to register
users.
The admin user is provided with a menu option that allows
them to display statistics. When this menu option is selected, the
total number of tasks and the total number of users are be
displayed in a user-friendly manner.

## Author
**Name:** JP Geyer  
**Email:** jpgeyergit@petalmail.com
