# class Point:
#     def __init__(self, x,y): ## this is constructor
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.move()
# point2.x = 1
#
# point = Point(10,20)
# print(point.x)

####### CONSTRUCTOR ######### A constructure is a function that gets called at the time of creating an object.
# class Person:
#     def __init__(self, name): # construtor
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# john = Person("John Smith")
# john.talk()
# bob = Person("Bob Smith")
# bob.talk()

####### INHERITENCE ####### A inheritance is a mechanism for using code.
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
