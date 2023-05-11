from human import Human


class Doctor(Human):
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

    def __str__(self):
        return f"{self.__name}: age = {self.__age}. " \
               f"Is alive? - {self.is_alive}. " \
               f"Has salary {self.__salary} RUB"
