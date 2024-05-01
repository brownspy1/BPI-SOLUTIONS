import csv
import os
# Function to read data from CSV
def read_from_csv():
    student_list = {}
    try:
        with open('student_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                roll = row['Roll']
                department = row['Department']
                name = row['Name']
                session = row['Session']
                student_list[roll] = {'Name': name, 'Department': department, 'Session': session}
        return student_list
    except FileNotFoundError:
        return {}  # Return empty dictionary if the file doesn't exist


# funcation for auth
credentials = {'bpi': '123'}


def login():
    user = input('Username: ')
    password = input('Password: ')  # Use getpass to input password securely
    if credentials.get(user) == password:
        return True
    else:
        print('Wrong username or password')
        return False


# Function to save data to CSV
def save_to_csv(student_list):
    with open('student_data.csv', 'w', newline='') as file:  # Use 'w' mode to overwrite the file
        fieldnames = ['Roll', 'Department', 'Name', 'Session']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for roll, info in student_list.items():
            writer.writerow(
                {'Roll': roll, 'Name': info['Name'], 'Department': info['Department'], 'Session': info['Session']})


def show_student(student_list):
    if not student_list:
        print('No students are listed')
    else:
        print('Name\t\t\tRoll\t\t\tDepartment\t\t\tSession')
        for roll, info in student_list.items():
            print("{}\t\t{}\t\t{}\t\t\t{}".format(info['Name'], roll, info['Department'], info['Session']))


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


