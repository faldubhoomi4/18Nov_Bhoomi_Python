class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    def show(self):
        print("Child Class")


ch = Child()
ch.show()  