class A:
    __length=0
    __width=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__width=w

    def area1(self):
        self.__area=self.__length*self.__width
        return self.__area
    def __gt__(self,other):
        if(self.__area>other.__area):
            return True
        else:
            return False

obj1=A(3,5)
print("\nArea of Obj-1",obj1.area1())
obj2=A(2,3)
print("\nArea of Obj-2",obj2.area1())
if(obj1>obj2):
    print("\nobj1 is greater than obj2\n")
else:
    print("\nobj2 is greater than obj1\n")