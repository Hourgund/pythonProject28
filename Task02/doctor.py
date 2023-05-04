class Doctor:
    def __init__(self, name='no name', age='0', alive=True, salary=0, experience=1):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__experience = experience

    def can_heal(self):
        print(self.__name + " can heal.")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def mark(self, experience):
        if isinstance(experience, int) and experience > 0:
            self.__experience = experience

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age=1):
        if 0 <= 120:
            self.__age = age

    @property
    def is_alive(self):
        return "Yes" if self.__alive else "No"

    @is_alive.setter
    def is_alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def __str__(self):
        return f"{self.__name}: age = {self.__age}. " \
               f"Is alive? - {self.is_alive}. " \
               f"Has salary {self.__salary} RUB"