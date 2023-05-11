class Super1:
    def walk(self):
        print("I can walk")


class Super2:
    def run(self):
        print("I can run")


class Subclass(Super1, Super2):
    pass


