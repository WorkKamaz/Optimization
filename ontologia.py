from abc import ABC, abstractmethod


# Класс управляющего персонала
class ManagerialStaff(ABC):
    def __init__(self, name, gender, salary, age):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.age = age
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def assign_supervisor(self, supervisor):
        self.supervisor = supervisor


# Менеджер
class Manager(ManagerialStaff):
    def __init__(self, name, gender, salary, age):
        super().__init__(name, gender, salary, age)
# Бухгалтер
class Accountant(ManagerialStaff):
    def __init__(self, name, gender, salary, age):
        super().__init__(name, gender, salary, age)
        self.supervisor = None

    def assign_supervisor(self, supervisor):
        self.supervisor = supervisor

# Обслуживающий персонал
class OperationalStaff(ABC):
    def __init__(self, name, gender, salary, age):
        self.gender = gender
        self.name = name
        self.age = age
        self.salary = salary
        self.subordinates = []

    def assign_supervisor(self, supervisor):
        self.supervisor = supervisor

# Создание управляющего персонала
manager_elena = Manager("Елена", "Ж", 86000, 42)
accountant_michail = Accountant("Михаил", "М", 80000, 26)
accountant_dmitriy = Accountant("Дмитрий", "М", 72000, 20)
accountant_anna = Accountant("Анна", "Ж", 78000, 26)
accountant_olga = Accountant("Ольга", "Ж", 50000, 21)

# Создание обслуживающего персонала
salesman_artem = OperationalStaff("Артем", "М", 32000, 18)
salesman_oleg = OperationalStaff("Олег", "М", 35000, 19)
salesman_danil = OperationalStaff("Данил", "М", 34000, 23)
cashier_vera = OperationalStaff("Ж", "Вера", 41, 23000)

courier_vitaliy = OperationalStaff("Виталий", "М", 100000, 21)
courier_vladimir = OperationalStaff("Владимир", "М", 60000, 20)

supplier_sergey = OperationalStaff("Сергей", "М", 20000, 35)

cleaner_anton = OperationalStaff("Антон", "М", 33000, 33)

# Назначение начальников
manager_elena.add_subordinate(accountant_michail)
manager_elena.add_subordinate(accountant_dmitriy)
manager_elena.add_subordinate(accountant_anna)
manager_elena.add_subordinate(accountant_olga)

manager_elena.add_subordinate(salesman_artem)
manager_elena.add_subordinate(salesman_oleg)
manager_elena.add_subordinate(salesman_danil)

# Назначение подчиненных
accountant_michail.assign_supervisor(manager_elena)
accountant_dmitriy.assign_supervisor(manager_elena)
accountant_anna.assign_supervisor(manager_elena)
accountant_olga.assign_supervisor(manager_elena)

salesman_artem.assign_supervisor(manager_elena)
salesman_oleg.assign_supervisor(manager_elena)
salesman_danil.assign_supervisor(manager_elena)

accountant_michail.add_subordinate(salesman_artem)
accountant_michail.add_subordinate(salesman_oleg)
accountant_michail.add_subordinate(salesman_danil)

salesman_artem.assign_supervisor(accountant_michail)
salesman_oleg.assign_supervisor(accountant_michail)
salesman_danil.assign_supervisor(accountant_michail)

accountant_dmitriy.add_subordinate(courier_vitaliy)
accountant_dmitriy.add_subordinate(courier_vladimir)

courier_vitaliy.assign_supervisor(accountant_dmitriy)
courier_vladimir.assign_supervisor(accountant_dmitriy)

accountant_anna.add_subordinate(supplier_sergey)
supplier_sergey.assign_supervisor(accountant_anna)
accountant_olga.add_subordinate(cleaner_anton)
cleaner_anton.assign_supervisor(accountant_olga)

# Запросы
def filter_staff(supervisor,
                 condition):  # определение функции filter_staff с двумя параметрами - supervisor и condition
    filtered_staff = []
    for subordinate in supervisor.subordinates:  # Происходит итерация по подчиненным, которые находятся в атрибуте subordinates объекта supervisor.
        if condition(
                subordinate):  # Каждый подчиненный проверяется условием, которое передается как функция condition.
            # Если условие выполняется для текущего подчиненного, то он добавляется в список filtered_staff.
            filtered_staff.append(subordinate)
            filtered_staff.extend(filter_staff(subordinate,
                                               condition))
  # вызывается рекурсивная функция filter_staff для текущего подчиненного
            # subordinate,и результат этой рекурсивной функции расширяет список filtered_staff.
            # Таким образом, рекурсивно обрабатываются все уровни подчиненных.
    return filtered_staff


def find_staff_by_name(supervisor, name):
    if supervisor.name == name:
        return supervisor

    for subordinate in supervisor.subordinates:
        if subordinate.name == name:
            return subordinate
        found_subordinate = find_staff_by_name(subordinate, name)
        if found_subordinate:
            return found_subordinate
    return None

# Вводим имя сотрудника
search_name = input("Введите имя сотрудника, чтобы вывести кому он подчиняется и кто подчиняется ему: ")

# Вывод по подчиненности
found_staff = find_staff_by_name(manager_elena, search_name)

# Вывод по подчиненности
if found_staff:
    print(f"Имя: {found_staff.name} ({found_staff.__class__.__name__})")
    if hasattr(found_staff, 'supervisor'):
        print(f"Начальник: {found_staff.supervisor.name} ({found_staff.supervisor.__class__.__name__})")
    if hasattr(found_staff, 'subordinates') and found_staff.subordinates:
        print("Подчиненные:")
        for subordinate in found_staff.subordinates:
            print(f"{subordinate.name} ({subordinate.__class__.__name__})")
    else:
        print("У этого сотрудника нет подчиненных.")
else:
    print(f"Сотрудник с именем {search_name} не найден.")


# Вывод по полу
# Функция для рекурсивного поиска всех сотрудников заданного пола
def find_staff_by_gender(supervisor, gender, result=None):
    if result is None:
        result = set()  # Используем множество для хранения уникальных имен сотрудников
    if hasattr(supervisor, 'gender') and supervisor.gender == gender:
        result.add(supervisor.name)
    for subordinate in supervisor.subordinates:
        if hasattr(subordinate, 'gender') and subordinate.gender == gender:
            result.add(subordinate.name)
        find_staff_by_gender(subordinate, gender, result)
    return list(result)

filter_by_gender = input("Хотите ли вы фильтровать сотрудников по полу? (да/нет): ").lower()

if filter_by_gender == "да":
    gender_filter = input("Введите пол для фильтрации (М/Ж): ").capitalize()
filtered_staff = find_staff_by_gender(manager_elena, gender_filter)
if filtered_staff:
    print("Сотрудники заданного пола:")
    for staff_name in filtered_staff:
        print(staff_name)

# Функция поиска по возрасту
def find_staff_by_age(supervisor, age, result=None):
    if result is None:
        result = set()  # Используем множество для хранения уникальных имен сотрудников
    if hasattr(supervisor, 'age') and supervisor.age > age:
        result.add(supervisor.name)
    for subordinate in supervisor.subordinates:
        if hasattr(subordinate, 'age') and subordinate.age > age:
            result.add(subordinate.name)
        find_staff_by_age(subordinate, age, result)
    return list(result)  # Преобразуем множество обратно в список для вывода
