class Empl():
    def __init__(self, id, name,):
        self.id = id
        self.name = name
        


class Freelance(Empl):
    def __init__(self, id, name, Emails):
        super().__init__(id, name,)
        self.Emails = Emails

Emp_1 = Freelance(101, "bhoomi", "Rajkot " , "faldubhoomi@gmail.com")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Emails is:', Emp_1.Emails)