class Calculator:
    def __init__(self) -> None:
        self.num1 = float(input("Enter the value for num1 : "))
        self.num2 = float(input("enter the value for num2 : "))
    
    def add(self):
        result_add = self.num1 + self.num2
        print(f"The sum is : {result_add}")
    
    def subtract(self):
        if self.num1 > self.num2:
            result_sub = self.num1 - self.num2
        else:
            result_sub = self.num2 - self.num1
        print(f"The Difference is : {result_sub}")
    
    def multiply(self):
        result_mul = self.num1 * self.num2
        print(f"The multiplied result is : {result_mul}")
    
    def divide(self):
        result_div = self.num1 / self.num2
        print(f"The division result is : {result_div}")

c1 = Calculator()
c1.add()
c1.subtract()
c1.multiply()
c1.divide()
