class Student:
    def __init__(self, sid: int, firstname: str, lastname: str):
        self.sid = sid
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"Student[{self.sid}: {self.firstname} {self.lastname}]"


class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, student: Student):
        self.students[student.sid] = student

    def get_student(self, sid: int) -> Student | None:
        return self.students.get(sid)

    def get_all_students(self) -> list[Student]:
        return list(self.students.values())

    def is_student_exists(self, sid: int) -> bool:
        return sid in self.students


class StudentInformationSystem:
    def __init__(self):
        self.db = StudentDatabase()

    def ui_main_menu(self):
        while True:
            print("\nStudent Information System")
            print("  [1] Add a student into the database.")
            print("  [2] Search for a student by id.")
            print("  [3] List all students.")
            result = input("  Choose one [1|2|3] or anything else to exit: ")
            try:
                match int(result):
                    case 1: self.ui_add_student()
                    case 2: self.ui_search_student()
                    case 3: self.ui_list_students()
                    case _: break
            except:
                break
        print("\nExit program normally.")

    def ui_input_student_id(self) -> int:
        while True:
            value = input("  Please type a valid student id and press Enter\n"
                        "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            sid = self.bl_transform_to_sid(value)
            if sid is not None:
                return sid
            print("  invalid student id format")

    def ui_input_new_student_id(self) -> int:
        while True:
            sid = self.ui_input_student_id()
            if not self.db.is_student_exists(sid):
                return sid
            print("  This student id already exists")

    def ui_input_student_name(self, name: str) -> str:
        while True:
            value = input(f"  Please type the student {name} and press Enter\n"
                        "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            if self.bl_validate_name(value):
                return value
            print("  Invalid student name format (whitespace is not allowed)")

    def ui_add_student(self):
        print("Adding a student into the database:")
        try:
            sid = self.ui_input_new_student_id()
            firstname = self.ui_input_student_name("firstname")
            lastname = self.ui_input_student_name("lastname")
            student = Student(sid, firstname, lastname)
            self.db.add_student(student)
            print(f"Student[{sid}: {firstname} {lastname}] is added into the database successfully.")
        except ValueError:
            print("  -- No student is added --")

    def ui_search_student(self):
        print("Searching for a student by student id:")
        try:
            sid = self.ui_input_student_id()
            student = self.db.get_student(sid)
            if student is None:
                print("  Student not found")
            else:
                print(f"  Student ID: {student.sid}, Firstname: {student.firstname}, Lastname: {student.lastname}")
        except ValueError:
            print("  -- No student to be searched --")

    def ui_list_students(self):
        students = self.db.get_all_students()
        if len(students) == 0:
            print("  -- No students in the database. --")
        for student in students:
            print(f"  Student ID: {student.sid}, Firstname: {student.firstname}, Lastname: {student.lastname}")

    @staticmethod
    def bl_transform_to_sid(sid: str) -> int | None:
        try:
            value = int(sid)
            if 67130500000 <= value <= 67130500999:
                return value
        except ValueError:
            pass
        return None

    @staticmethod
    def bl_validate_name(name: str) -> bool:
        if type(name) is not str or ' ' in name or '\t' in name or '\n' in name:
            return False
        return True


def main():
    system = StudentInformationSystem()
    system.ui_main_menu()


if __name__ == "__main__":
    main()
