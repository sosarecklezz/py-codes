class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius**2*3.147
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(9)
print(NewCircle.area())
print(NewCircle.perimeter())
