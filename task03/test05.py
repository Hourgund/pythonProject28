class Super:
    def walk(self):
        print("I can walk")


class Subclass(Super):
    pass


base = Super()
sub = Subclass()

print(f"Is subclass Super? - {issubclass(Subclass, Super)}")
print(f"Is Super Subclass? - {issubclass(Super, Subclass)}")
print(f"Is Super oblect? - {issubclass(Super, object)}")
print(f"Is Subclass oblect? - {issubclass(Subclass, object)}")