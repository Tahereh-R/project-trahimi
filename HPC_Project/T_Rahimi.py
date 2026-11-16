# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']



# Generate a report for the entire week
def report_week(habits, tasks, file_name):

    print("\nWeekly Report for:", file_name)

    # Create two empty lists for completed and incomplete tasks
    completed_tasks = []
    incomplete_tasks = []

    # Go through each day and collect the tasks
    for day in days:

        for task_name, status in tasks[day].items():

            if status == True:
                completed_tasks.append(task_name + " (" + day + ")")
            else:
                incomplete_tasks.append(task_name + " (" + day + ")")

    # Display completed tasks
    print("\nCompleted Tasks:")

    if completed_tasks:
        for task in completed_tasks:
            print("✅", task)
    else:
        print("No completed tasks.")

    # Display incomplete tasks
    print("\nIncomplete Tasks:")

    if incomplete_tasks:
        for task in incomplete_tasks:
            print("❌", task)
    else:
        print("No incomplete tasks.")

    # Display weekly habit progress
    print("\nWeekly Habits:")

    if not habits:
        print("No habits found.")

    else:
        for habit_name, status in habits.items():

            completed_days = 0

            # Count how many days the habit was completed
            for day in days:
                if status[day] == True:
                    completed_days += 1

            print(habit_name, ":", completed_days, "/7 days complete")

    print("\nEnd of Weekly Report") 



# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.

file_list = [
    "dictionaries_1.txt",
    "dictionaries_2.txt",
    "dictionaries_3.txt",
    "dictionaries_4.txt",
    "dictionaries_5.txt",
    "dictionaries_6.txt",
    "dictionaries_7.txt",
    "dictionaries_8.txt",
    "dictionaries_9.txt",
    "dictionaries_10.txt"
]


# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.


for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        report_week(data[0], data[1], file_name)