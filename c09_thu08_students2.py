# GroupName in LEB2: c09_thu00
# FileName: c09_thu00_students2.py
# member list in the file
# 073 ชัยบดินทร์
# 106 ภาคิน
# 108 ภูดิศ
# 109 ยุทธภูมิ
# 117 ศุภฤกษ์

def main():
    list_of_dicts = []  # list of dict {"id": ..., "name": ..., "lastname": ...}
    dict_of_lists = {"ids": [], "names": [], "lastnames": []}  # dict of 3 lists with keys:
    ask = ""
    while ask != "yes" and ask != "y":
        ask = input("do u want to add members (yes/no) : ")
        if ask.lower() == "no" or ask == "n":
            # print_students_from_dict(list_of_dicts)
            # print_students_from_list(dict_of_lists)
            break
        id, name,lastname = read_one_student()
        add_student_to_dict(list_of_dicts, id, name, lastname)
        add_student_to_lists(dict_of_lists, id, name, lastname)
    # if yes,
    #    call read_one_student() that read id, name, and lastname
    #    call add_student_to_dict(list_of_dicts, id, name, lastname)
    #    call add_student_to_lists(dict_of_lists, id, name, lastname)
    # if no,
    #    call print_students_from_dict(list_of_dicts)
    #    call print_students_from_lists(dict_of_lists)
    ######### Note: print 1 student per line

def read_one_student() -> (int, str, str):
    while True:
        try:
            id = int(input('input ur id : '))
            if 67130501000 > id >= 67130500000:
                break
        except ValueError:
            print("Error")
    name = input('input ur firstname : ')
    lastname = input('input ur lastname : ')
    return id, name, lastname

def add_student_to_dict(students: list, id: int, name: str, lastname: str):
    print('add_student_to_dict ok')
    students = []
    dict = {'ids': id, 'names': name, 'lastnames': lastname, }
    students.append(dict)
    print(students)

def add_student_to_lists(students: dict, id: int, name: str, lastname: str):
    print('add_student_to_lists ok')
    students = {"ids": [], "names": [], "lastnames": []}
    students['ids'].append(id)
    students['names'].append(name)
    students['lastnames'].append(lastname)
    print(students)

# add id, name, lastname to "ids" list, "names" list, and "lastnames" list

def print_students_from_dict(students):
    print('print_students_from_dict ok')
    print(students)
    for i in range(len(students['ids'])):
        print(f"id: {students['ids'][i]}, name: {students['names'][i]}, lastname: {students['lastnames'][i]}")

# print each student in students list

# def print_students_from_list(students):
# print each student in "ids", "names", and "lastnames" lists

if __name__ == "__main__":
    main()
