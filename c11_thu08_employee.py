# group name: c11_thu00
# file name: c11_thu00_employee.py
# 073 ชัยบดินทร์
# 106 ภาคิน
# 108 ภูดิศ
# 109 ยุทธภูมิ
# 117 ศุภฤกษ์
# deadline thu-31-10-2024 before 14:00

class Employee:
    def __init__(self, eid: int, name: str, salary: float):
        self._eid = eid
        self._name = name
        self._salary = salary

    def __repr__(self):
        return  "fuck"

    def get_name(self):
        return self._name

    def compare(self,another):
        if self._eid != another._eid:
            return False


emp = Employee(0,"ky",0)
emp1 = Employee(1,"1",1)
print(emp)
print(emp.get_name())
print(emp.compare(emp1))

# fields: eid: int, name: str, salary: float
# methods: get_eid(), get_name(), get_salary(),
#    set_name(new_name), set_salary(new_salary),
#    constructor(eid, name, salary)
#    representation: Employee(eid: ..., name: ..., salary: ...)
#
# sample code to use the class
#
# special points:
#   method: compare(another_employee)
#      return -1 if this employee.eid < another_employee.eid
#      return 0 if the two employees have the same eid
#      return 1 if this employee.eid > another_employee.eid
