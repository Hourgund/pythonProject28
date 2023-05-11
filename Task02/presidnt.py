from human import Human


class President(Human):
    def __init__(self, name='no name', age='0', alive=True, power=50):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__power = power

    def can_rule(self):
        print(self.__name + " can rule.")

    @property
    def power(self):
        return self.__power

    @power.setter
    def mark(self, power):
        if isinstance(power, int) and 0 < power <= 100:
            self.__power = power

    def __str__(self):
        return f"{self.__name}: age = {self.__age}. " \
               f"Is alive? - {self.is_alive}. " \
               f"Has salary {self.__salary} RUB"
