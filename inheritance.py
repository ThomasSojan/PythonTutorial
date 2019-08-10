class Mammal:
    def walk(self):
        print("walking")
class Dog(Mammal):
    def talk(self):
        print("Bow bow.....")
class Cat(Mammal):
    def talk(self):
        print("Meow meow....")        

rocky = Dog()
rocky.talk()
rocky.walk()

pussy = Cat()
pussy.talk()
pussy.walk()
