from doctor import Doctor
from worker import Worker
from presidnt import President
from student import Student


def main():
    doc = Doctor("Watson", 55, True, 35)
    student = Student("Alex", 20, True, 10)
    president = President("Trueman", 60, True, 80)
    worker = Worker("Volodya", 45, True, 2500)

    print(doc)
    doc.can_heal()

    print(student)
    student.can_study()

    print(worker)
    worker.can_work()

    print(president)
    president.can_rule()


if __name__ == "__main__":
    main()
