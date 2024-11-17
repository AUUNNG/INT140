"""
c13 assignment
group id: c13_thu00
file submission: c13_thu00_fp.py
"""
# member list in the file
# 073 chaibadin seajew
# 106 Pakin siripat
# 108 Pudit Patdipan
# 109 yutthaphum haphanom
# 117 supalerk kamolnetr

from typing import Callable
from functools import reduce

class Employee:
    def __init__(self, eid: int, name: str, salary: float):
        self._eid = eid
        self._name = name
        self._salary = salary

    def get_eid(self) -> int:
        return self._eid
    
    def get_name(self) -> str:
        return self._name
    
    def get_salary(self) -> float:
        return self._salary
    
    def set_eid(self, eid: int):
        self._eid = eid

    def set_name(self, name: str):
        self._name = name

    def set_salary(self, salary: float):
        self._salary = salary
    
    def __str__(self) -> str:
        return f"Employee(EID: {self._eid}, Name: {self._name}, Salary: {self._salary})"

employees = [
    Employee(1, "Alice", 1500.0),
    Employee(2, "Bob", 800.0),
    Employee(3, "Charlie", 2000.0),
    Employee(4, "David", 1200.0),
    Employee(5, "Eve", 950.0),
    Employee(6, "Frank", 2100.0)
]

def filter_high_salary(employees: list) -> list:
    return list(filter(lambda e: e.get_salary() > 1000, employees))

def map_employee_names(employees: list) -> list:
    return list(map(lambda e: e.get_name(), employees))

def average_salary(employees: list) -> float:
    total_salary = reduce(lambda acc, e: acc + e.get_salary(), employees, 0.0)
    return total_salary / len(employees) if employees else 0.0

def filter_employees(employees: list, filter_func: Callable) -> list:
    return list(filter(filter_func, employees))

def map_employees(employees: list, map_func: Callable) -> list:
    return list(map(map_func, employees))

def reduce_employees(employees: list, reduce_func: Callable, initial: float) -> float:
    return reduce(reduce_func, employees, initial)

def main():
    high_salary_employees = filter_high_salary(employees)
    print("Employees with salary > 1000:")
    for e in high_salary_employees:
        print(e)

    employee_names = map_employee_names(employees)
    print("\nEmployee Names:")
    print(employee_names)

    avg_salary = average_salary(employees)
    print(f"\nAverage Salary: {avg_salary:.2f}")

    high_salary = filter_employees(employees, lambda e: e.get_salary() > 1000)
    print("\nGeneralized Filtered Employees (salary > 1000):")
    for e in high_salary:
        print(e)

    names = map_employees(employees, lambda e: e.get_name())
    print("\nGeneralized Mapped Employee Names:")
    print(names)

    total_salary = reduce_employees(employees, lambda acc, e: acc + e.get_salary(), 0.0)
    print(f"\nTotal Salary: {total_salary:.2f}")
    print(f"Average Salary (via reduce): {total_salary / len(employees):.2f}")

if __name__ == "__main__":
    main()
