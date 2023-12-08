class Student:
    
    def __init__(self) -> None:
        self.__name = input("Enter the name : ")
        self.__rollnumber = input("Enter the roll no : ")
    
    def getName(self):
        return self.__name
    
    def getRollNumber(self):
        return self.__rollnumber
    
    def setName(self, new_name):
        self.__name = new_name
    
    def setRollNumber(self, new_num):
        self.__rollnumber = new_num

s1 = Student()
print(s1.getName(), s1.getRollNumber())

s1.setName("Bob"), s1.setRollNumber(102)
print(s1.getName(), s1.getRollNumber())
