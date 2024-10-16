# GroupName in LEB2: c09_thu00
# FileName: c09_thu00_students2.py
# member list in the file
# 073 ชัยบดินทร์
# 106 ภาคิน
# 108 ภูดิศ
# 109 ยุทธภูมิ
# 117 ศุภฤกษ์

def main():
    list_of_dicts = []
    dict_of_lists = {"ids": [], "names": [], "lastnames": []}
    ask = ""
    while True:
        print('')
        ask = input("do u want to add members (yes/no/end) : ")
        ask.lower()
        if ask == "no" or ask == "n":
            print_students_from_dict(list_of_dicts)
            print_students_from_lists(dict_of_lists)
        if ask == "yes" or ask == "y":
            id, name,lastname = read_one_student()
            list_of_dicts = add_student_to_dict(list_of_dicts, id, name, lastname)
            dict_of_lists = add_student_to_lists(dict_of_lists, id, name, lastname)
        if ask == "end":
            print('system> end')
            break

def read_one_student() -> (int, str, str):
    while True:
        try:
            id = int(input('input ur id : '))
            if 67130501000 > id >= 67130500000:
                break
        except ValueError:
            print("system> Error")
    name = input('input ur firstname : ')
    lastname = input('input ur lastname : ')
    return id, name, lastname

def add_student_to_dict(students: list, id: int, name: str, lastname: str) -> (list):
    print('system> add_student_to_dict ok')
    dict = {'ids': id, 'names': name, 'lastnames': lastname, }
    students.append(dict)
    return students

def add_student_to_lists(students: dict, id: int, name: str, lastname: str) -> (dict):
    print('system> add_student_to_lists ok')
    students['ids'].append(id)
    students['names'].append(name)
    students['lastnames'].append(lastname)
    return students

def print_students_from_dict(students):
    print('')
    print('system> print_students_from_dict ok')
    print(students)
    for student in students:
        print(f"ID: {student['ids']}, Name: {student['names']}, Lastname: {student['lastnames']}")

def print_students_from_lists(students):
    print('')
    print('system> print_students_from_lists ok')
    print(students)
    for i in range(len(students['ids'])):
        print(f"ID: {students['ids'][i]}, Name: {students['names'][i]}, Lastname: {students['lastnames'][i]}")

if __name__ == "__main__":
    main()
