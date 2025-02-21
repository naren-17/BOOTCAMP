class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

def animal_speak(animal):
    print(animal.speak())

my_dog = Dog()
my_cat = Cat()
animal_speak(my_dog)  
animal_speak(my_cat)  
