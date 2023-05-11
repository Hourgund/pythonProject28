class Super:
    def __init__(self, name='Alex'):
        self._name = name

    def walk(self):
        print("I can walk")

    @property
    def name(self):
        return self._name

    @staticmethod
    def smethod():
        print("static method from Super class")

    @classmethod
    def cmehtod(cls):
        print("class method from Super class")

    def function(a, b):
        c = a + b
        print(c)


class Subclass(Super):
    pass


sub = Subclass("Peter Pan")
sub.walk()

print(sub._name)
print(sub.name)
Subclass.smethod()
sub.smethod()
Subclass.cmehtod()
sub.cmehtod()
Subclass.function(4, 5)
