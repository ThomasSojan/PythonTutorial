class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"{self.name} is talking")


person1 = Person("John")
print(person1.name)
person1.talk()

person2 = Person('Thomas')
person2.talk()



