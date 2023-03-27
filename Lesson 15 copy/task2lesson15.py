class Dog:
    
    age_factor = 7
    def __init__(self, d_age):
        self.d_age = d_age
    
    def human_age(self):
        return self.d_age * self.age_factor
    
dog = Dog(8)
print(dog.human_age()) 