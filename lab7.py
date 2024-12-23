class Employee:
    def __init__(self, name, id, **kwargs):
        self.name = name
        self.id = id
        super().__init__(**kwargs)

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department, **kwargs):
        super().__init__(name, id, **kwargs)
        self.department = department

    def manage_project(self):
        return f"Сотрудник {self.name} управляет проектами в отделе {self.department}."


class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Сотрудник {self.name} выполняет техническое обслуживание по специализации: {self.specialization}."


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization, **kwargs):
        super().__init__(name, id, department=department, specialization=specialization, **kwargs)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = "Информация о команде:\n"
        for member in self.team:
            team_info += member.get_info() + "\n"
        return team_info


# создаем сотрудников
empl = Employee('Ромашков Роман Степанович', 119000)
mgr = Manager('Белоусова Марина Геннадьевна', 119059, 'по работе с персоналом')
tech = Technician('Романов Алексей Михайлович', 119856, 'сварка')
tech_mgr = TechManager('Васильева Мария Александровна', 119470, 'ИТ', 'Системный администратор')
# добавляем сотрудников в команду
tech_mgr.add_employee(empl)
tech_mgr.add_employee(mgr)
tech_mgr.add_employee(tech)

print(tech_mgr.get_team_info())

print('Проверка:')
print(empl.get_info())
print(mgr.manage_project())
print(tech.perform_maintenance())