class Point:
    def __init__(self) -> None:
        self.x = int(input("enter the value for x: "))
        self.y = int(input("enter the value for y: "))
        self.z = int(input("enter the value for z: "))
        
    def sqSum(self):
        result = (self.x ** 2) + (self.y ** 2) + (self.z ** 2) 
        return result

#creating an instance of class Point
p1 = Point()

#calculating the square sum and printing the result
print(f"The square Sum of x,y,z is: {p1.sqSum()}")
