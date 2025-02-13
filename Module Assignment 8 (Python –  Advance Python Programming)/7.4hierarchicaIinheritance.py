class Student: 
    id = 101
    name = "bhoomi"
    def printdata(self):
        print("Welcome to tops technology student")
    
    
class result(Student):
    def marksheet(self, sub1, sub2):
        print("sub1 marks:", sub1)
        print("sub2 marks:", sub2)
        print("total marks:", sub1+sub2)

class address(Student):
    def add(self, city):
        s1add = input("Enter your address: ")
        city = input("Enter Your City: ")
        print("Your address is a ", s1add, city)
        
add = address()
rs = result() 
add.printdata()

print("ID:", add.id)
print("Name:", add.name)
rs.marksheet(70, 45)
add.add("Rajkot")


