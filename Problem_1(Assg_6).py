import json

class Employee_details():
    
    employee_list = []
    
    def __init__(self, name, dob, height, city, state):
        self.Name = name
        self.DOB = dob
        self.Height = height
        self.City = city
        self.State = state
    
    @classmethod
    def create_list(cls):
        emp_data = json.load(open("employee.json"))
        for each_data in emp_data:
            emp = Employee_details(each_data["Name"], each_data["DOB"], each_data["Height"], each_data["City"], each_data["State"])
            cls.employee_list.append(emp)
        return cls.employee_list
        
employee_objects = Employee_details.create_list()
for emp_obj in employee_objects:
    print(vars(emp_obj))
