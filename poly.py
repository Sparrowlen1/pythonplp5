class Animal:
    def move(self):
        print("The animal moves...")

class Dog(Animal):
    def move(self):
        print("Running on four legs!")

class Bird(Animal):
    def move(self):
        print("Flying in the sky!")

class Fish(Animal):
    def move(self):
        print("Swimming in water!")

# Vehicles Example
class Vehicle:
    def move(self):
        print("The vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water!")

# Testing polymorphism
animals = [Dog(), Bird(), Fish()]
vehicles = [Car(), Plane(), Boat()]

print("\n--- Animal Moves ---")
for a in animals:
    a.move()

print("\n--- Vehicle Moves ---")
for v in vehicles:
    v.move()
