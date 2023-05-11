from human import Human


class President(Human):
    def __init__(self, name='no name', age='0', alive=True, power=50):
        super().__init__(name, age, alive)
        self.__power = power

    def can_rule(self):
        print(self.name + " can rule.")

    @property
    def power(self):
        return self.__power

    @power.setter
    def mark(self, power):
        if isinstance(power, int) and 0 < power <= 100:
            self.__power = power

    def __str__(self):
        return (super().__str__()
                + f" Has salary {self.__power} RUB")
