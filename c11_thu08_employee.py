class Employee:
    # Constructor
    def __init__(self, eid: int, name: str, salary: float):
        self.eid = eid
        self.name = name
        self.salary = salary

    # Methods to get values
    def get_eid(self) -> int:
        return self.eid

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return self.salary

    # Methods to set new values
    def set_name(self, new_name: str):
        self.name = new_name

    def set_salary(self, new_salary: float):
        self.salary = new_salary

    # Method to compare employees based on eid
    def compare(self, another_employee) -> int:
        if self.eid < another_employee.eid:
            return -1
        elif self.eid == another_employee.eid:
            return 0
        else:
            return 1

    # String representation of the Employee object
    def __repr__(self) -> str:
        return f"Employee(eid: {self.eid}, name: {self.name}, salary: {self.salary})"

# สร้างอ็อบเจ็กต์ของ Employee
employee1 = Employee(101, "John Doe", 50000)
employee2 = Employee(102, "Jane Smith", 55000)

# ใช้งานเมธอดต่างๆ
print(employee1.get_name())  # "John Doe"
print(employee1.get_salary())  # 50000

# เปรียบเทียบพนักงาน
print(employee1.compare(employee2))  # -1 (เพราะ 101 < 102)

# แสดงผลการเปรียบเทียบ
print(employee1)  # Employee(eid: 101, name: John Doe, salary: 50000)
