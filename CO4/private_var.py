class privatedemo:
    __num=0
    def count(self):
        self.__num+=1
        print(self.__num)
number=privatedemo()
number.count()
number.count()
print(number.__num)
#print(number.__num)

#Data Hiding
#Cannot access a variable(defined inside the class) from outside.