class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print(f"{self.name} is barking")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Cat:
    def __init__(self, name):
        self.name = name
        
    def meow(self):
        print(f"{self.name} is meowing")
        
    def purr(self):
        print(f"{self.name} is purring")
        
class Hybrid(Dog, Cat):
    def __init__(self, name):
        super().__init__(name)
        
my_hybrid = Hybrid("doct")
my_hybrid.bark()
my_hybrid.sleep()
my_hybrid.meow()
