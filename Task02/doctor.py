from human import Human


class Doctor(Human):
    def __init__(self, name='no name', age='0', alive=True, salary=0, experience=1):
        super().__init__(name, age, alive)
        self.__experience = experience

    def can_heal(self):
        print(self.name + " can heal.")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def mark(self, experience):
        if isinstance(experience, int) and experience > 0:
            self.__experience = experience

    def __str__(self):
        return (super().__str__() +
                f" Has experience {self.__experience} RUB")
