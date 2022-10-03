
#   StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName

data = []


def data_reader(data):
    f = open("students.txt", "r")
    lines = f.readlines()
    for line in lines:
        cur_line = line.strip().split(',')
        cur_student_info = {
            "StLastName": cur_line[0],
            "StFirstName": cur_line[1],
            "Grade": cur_line[2],
            "Classroom": cur_line[3],
            "Bus": cur_line[4],
            "GPA": cur_line[5],
            "TLastName": cur_line[6],
            "TFirstName": cur_line[7]
        }
        data.append(cur_student_info)


data_reader(data)


# [{'StLastName': 'COOKUS', 'StFirstName': 'XUAN', 'Grade': '3', 'Classroom': '107',
#  'Bus': '52', 'GPA': '3.07', 'TLastName': 'FAFARD', 'TFirstName': 'ROCIO'},
#  {'StLastName': 'SCHOENECKER', 'StFirstName': 'PHUONG', 'Grade': '6', 'Classroom': '109',
#      'Bus': '0', 'GPA': '3.15', 'TLastName': 'GAMBREL', 'TFirstName': 'JAE'},
#  ...]

user_instruction = input("Please enter an instruction:")
cmd_key, cmd_value = user_instruction.split(
    ':')[0].strip(), user_instruction.split(':')[1].strip().split()
search_initial = cmd_key[0]
search_value_one = cmd_value[0]
search_value_two = None
multiple_values_existed = True

if len(cmd_value) > 1:
    search_value_two = cmd_value[1]
else:
    multiple_values_existed = False


def data_fetcher(data, search_initial, search_value_one, search_value_two):
    # print template:
    # Sherman Drop, who takes bus route 51, is a kindergarten student assigned to the class
    # of Jerlene Nibler in the classroom 104. Sherman has a GPA of 2.65.

    for d in data:
        student_ln = d["StLastName"]
        student_fn = d["StFirstName"]
        student_grade = d["Grade"]
        student_classroom = d["Classroom"]
        student_bus = d["Bus"]
        student_gpa = d["GPA"]
        teacher_ln = d["TLastName"]
        teacher_fn = d["TFirstName"]

        # R4, R5
        # For each entry found, print the last name, first name,
        # grade and classroom assignment for each student found and the name of their teacher (last and first name).
        if search_initial == 'S':
            if student_ln == search_value_one:
                # R4 S[tudent]: <lastname>
                # print last name, first name, grade and classroom assignment and the name of their teacher (last and first name).
                if search_value_two == None:
                    return f"{student_ln}, {student_fn}, {student_grade}, {student_classroom}, {teacher_ln}, {teacher_fn}"
                else:
                    # R5 S[tudent]: <lastname> B[us]
                    # print the last name, first name and the bus route the student takes.
                    return f"{student_ln}, {student_fn}, {student_bus}"

        # R6. T[eacher]: <lastname>
        # For each entry found, print the last and the first name of the student.
        if search_initial == 'T':
            if teacher_ln == search_value_one:
                # print the last and the first name of the student.
                pass


print(data_fetcher(data, search_initial, search_value_one, search_value_two))
