# read student.txt file and store each student's information into a data varibale
def data_reader():
    data = []
    f = open("students.txt", "r")
    lines = f.readlines()
    count = 0  # used as a referrence for the number of last loop in data_fetcher()

    for line in lines:
        count += 1
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
    return [data, count]


# get user's valid input/instruction
def get_instruction():

    while True:
        restart = False
        search_initial = ''
        search_value_one = None
        search_value_two = None

        try:
            user_instruction = input("Please enter an instruction:")
            user_instruction = user_instruction
            if user_instruction in ["Q", "QUIT"] or user_instruction in ["I", "QUIT"]:
                search_initial = user_instruction[0]
                break
            else:
                cmd_key, cmd_value = user_instruction.split(
                    ':')[0].strip(), user_instruction.split(':')[1].strip().split()

                search_initial = cmd_key[0]
                search_value_one = cmd_value[0]
                # if user's input has multiple conditions
                if len(cmd_value) > 1:
                    search_value_two = cmd_value[1][0]

                break
        except:
            pass
        print("Please enter a valid instruction:(")

    return [search_initial, search_value_one, search_value_two]


# fetch and process data, and generate outputs
def data_fetcher(data, search_initial, search_value_one, search_value_two, number_of_line):
    temp_gpa = 0
    highest_temp_gpa = float("-inf")
    lowest_temp_gpa = float("inf")
    temp_student_count = 0
    temp_student_info = ""
    temp_student_obj = {}

    for idx, item in enumerate(data):
        student_ln = item["StLastName"]
        student_fn = item["StFirstName"]
        student_grade = item["Grade"]
        student_classroom = item["Classroom"]
        student_bus = item["Bus"]
        student_gpa = item["GPA"]
        teacher_ln = item["TLastName"]
        teacher_fn = item["TFirstName"]

        # R4, R5
        # For each entry found, print the last name, first name,
        # grade and classroom assignment for each student found and the name of their teacher (last and first name).
        if search_initial == 'S':
            if student_ln == search_value_one:
                # R4 S[tudent]: <lastname>
                # print last name, first name, grade and classroom assignment and the name of their teacher (last and first name).
                if search_value_two == None:
                    print(
                        f"{student_ln}, {student_fn}, {student_grade}, {student_classroom}, {teacher_ln}, {teacher_fn}")
                else:
                    # R5 S[tudent]: <lastname> B[us]
                    # print the last name, first name and the bus route the student takes.
                    print(f"{student_ln}, {student_fn}, {student_bus}")

        # R6. T[eacher]: <lastname>
        # For each entry found, print the last and the first name of the student.
        if search_initial == 'T':
            if teacher_ln == search_value_one:
                # print the last and the first name of the student.
                print(f"{student_ln}, {student_fn}")

        # R9. G[rade]: <Number> H[igh] or G[rade]: <Number> L[ow]
        # find the entry in the students.txt file for the given grade with the highest GPA.
        # Report the contents of this entry (name of the student, GPA, teacher, bus route).

        if search_initial == 'G' and search_value_two == 'H':
            if student_grade == search_value_one:
                if float(student_gpa) > highest_temp_gpa:
                    highest_temp_gpa = float(student_gpa)
                    temp_student_info = ''
                    temp_student_info = f"{student_ln}, {student_fn}, {student_gpa}, {teacher_ln}, {teacher_fn}, {student_bus}"
            if idx == number_of_line-1:
                print(temp_student_info)

        if search_initial == 'G' and search_value_two == 'L':
            if student_grade == search_value_one:
                if float(student_gpa) < lowest_temp_gpa:
                    lowest_temp_gpa = float(student_gpa)
                    temp_student_info = ''
                    temp_student_info = f"{student_ln}, {student_fn}, {student_gpa}, {teacher_ln}, {teacher_fn}, {student_bus}"
            if idx == number_of_line-1:
                print(temp_student_info)

        # R7. G[rade]: <Number>
        # For each entry, output the name (last and first) of the student.
        if search_initial == 'G' and search_value_two == None:
            if student_grade == search_value_one:
                temp_student_info += f"{student_ln}, {student_fn} "
            if idx == number_of_line-1:
                print(temp_student_info)

        # R8. B[us]: <Number>
        # For each such entry, output the name of the student (last and first) and their grade and classroom.
        if search_initial == 'B':
            if student_bus == search_value_one:
                print(
                    f"{student_ln}, {student_fn}, {student_grade}, {student_classroom}")

        # R10. A[verage]: <Number>
        # Compute the average GPA score for the entries found.
        # Output the grade level (the number provided in command) and the average GPA score computed.
        if search_initial == 'A':
            if student_grade == search_value_one:
                temp_gpa += float(student_gpa)
                temp_student_count += 1
            if idx == number_of_line-1:
                ave_gpa = temp_gpa//temp_student_count
                print(f"{search_value_one}, {ave_gpa}")

        # R11. I[nfo]
        # Report the number of students in each grade in the format <Grade>: <Number of Students>
        # sorted in ascending order by grade.
        if search_initial == 'I':
            temp_student_obj[student_grade] = temp_student_obj.get(
                student_grade, 0)+1
            if idx == number_of_line-1:
                print(temp_student_obj)
                for Grade, Number_of_Students in temp_student_obj.items():
                    print(f"{Grade} : {Number_of_Students}")


def main():
    data, number_of_line = data_reader()
    search_commands = """ 
        • S[tudent]: <lastname> [B[us]]
        • T[eacher]: <lastname>
        • B[us]: <number>
        • G[rade]: <number> [H[igh]|L[ow]] 
        • A[verage]: <number>
        • I[nfo]
        • Q[uit]
        """
    print(search_commands)
    while True:
        search_initial, search_value_one, search_value_two = get_instruction()
        # R12. Q[uit]
        # When this instruction is issued your program shall quit the current session.
        if search_initial == 'Q':
            break
        data_fetcher(data, search_initial, search_value_one,
                     search_value_two, number_of_line)


main()
