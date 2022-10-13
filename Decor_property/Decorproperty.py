class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    @property
    def mag(self):
        return self.name + " got grade " + self.grade

    @msg.setter
    def msg (self,msg):
        sent = msg.split(" ")
        print(sent)
        self.name = sent [0]
        self.grade = sent [-1]

stud1 = Student("nia","B")
stud1.msg = "amulya got grade A"
print("name:",stud1.name)
print("grade:",stud1.grade)
print(stud1.msg)