from human import Human


class Worker(Human):
    def __init__(self, name='no name', age='0', alive=True, salary=0):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__salary = salary

    def can_work(self):
        print(self.__name + " can work.")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def mark(self, salary):
        if isinstance(salary, int) and salary > 0:
            self.__salary = salary

    def __str__(self):
        return f"{self.__name}: age = {self.__age}. " \
               f"Is alive? - {self.is_alive}. " \
               f"Has salary {self.__salary} RUB"
