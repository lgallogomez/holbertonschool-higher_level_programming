class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hi(self):
        print('Hello, my name is {}, im {} years old, and im a {}'.format(self.name, self.age, self.gender))

p = Person('oscar', 54,)
p.say_hi()