class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length    
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return (2*(self.length+self.breadth))
    def display(self):
        print("Area:",self.area())
        print("Perimeter:",self.perimeter())
    def __eq__(self, other):
        if self.area==other.area:
            return "Both objects are equal"
        else:
            return "They are unequal"
    def __lt__(self, other):
        a=self.area()
        b=other.area()
        if a<b:
            return "First object smaller than the other"
        else:
            return "First object larger than the other"

s1=rectangle(5,4)
s2=rectangle(4,3)
print("Rectangle 1:")
s1.display()
print("\nRectangle 2:")
s2.display()
print(s1<s2)


 