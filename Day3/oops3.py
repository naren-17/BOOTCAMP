#inheritence 

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} is barking")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def play(self):
        print(f"{self.name} is playing")
        
my_puppy = Puppy("Oreo", 1)
my_puppy.bark()
my_puppy.sleep()
my_puppy.play()
    