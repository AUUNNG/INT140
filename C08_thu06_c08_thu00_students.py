# GroupName in LEB2: c08_thu00
# FileName: c08_thu00_students.py
# member list in the file
# 073 ชัยบดินทร์
# 106 ภาคิน
# 108 ภูดิศ
# 109 ยุทธภูมิ
# 117 ศุภฤกษ์

# def student_data(all: list, id: int, name: str, lastname: str):
# build a list of (id, name, lastname)
# append this list to all

def read_one_member(all: list):
    firstname = input("input ur firstname : ")
    lastname = input("input ur lastname : ")
    id = input("input ur id : ")
    while 

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