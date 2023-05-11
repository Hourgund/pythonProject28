class Super:
    def walk(self):
        print("I can walk")


class Subclass(Super):
    pass


base = Super()
sub = Subclass()

print(f"Is base super? - {isinstance(base, Super)}")
print((f"Is base Subclass? - {isinstance(base, Subclass)}"))
print(f"Is base super? - {isinstance(sub, Super)}")
print((f"Is base Subclass? - {isinstance(sub, Subclass)}"))