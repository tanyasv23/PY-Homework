class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.")

person1 = Person("Alex", "Wilson", 23)
person2 = Person("Mark", "Davies", 34)
person3 = Person("Carol", "Brown", 20)

person1.talk()
person2.talk()
person3.talk()
