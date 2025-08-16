class Employee:
    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, payraise=5000):
        self.salary += payraise