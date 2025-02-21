class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} is barking")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def nage(self):
        print(f"{self.name} is {self.age} years old")
        
dog1 = Dog("Roger", 5)
dog1.bark()
dog1.sleep()
dog1.nage()