# GroupName in LEB2: c08_thu00
# FileName: c08_thu00_students.py
# member list in the file
# 073 ชัยบดินทร์
# 106 ภาคิน
# 108 ภูดิศ
# 109 ยุทธภูมิ
# 117 ศุภฤกษ์

def student_data(all: list, id: int, name: str, lastname: str):
    all.append(id)
    all.append(name)
    all.append(lastname)
    print(all)

def read_one_member(all: list):
    name = input("input ur firstname : ")
    lastname = input("input ur lastname : ")
    id = ""
    while True:
        id = input("input ur id: ")
        if len(id) < 10:
            print('id must be 11 digits')
            continue
        try:
            id = int(id)
            break
        except ValueError:
            print('input not correct')
    print('id correct')
    student_data(all, id, name, lastname)


# read id, name, lastname from user input
# validate id: 67130500XXX (loop until id is correct)
# add it to all by calling student_data

def main():
    students = []
    ask = ""
    while ask != "yes" and ask != "y":
        ask.lower()
        ask = input("do u want to add members (yes/no) : ")
        if ask == "no" or ask == "n":
            print("end")
            break
    read_one_member(students)

if __name__ == "__main__":
    main()
