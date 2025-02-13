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

rs = result()

rs.printdata()
print("ID:", rs.id)
print("Name:", rs.name)
rs.marksheet(90,95)


