class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__seconds=s
        
    def time(self):
        if self.__seconds>=60:
            self.__seconds-=60
            self.__minute +=1
        if self.__minute>=60:
            self.__minute-=60
            self.__hour +=1
        return("%.2d:%.2d:%.2d"%(self.__hour,self.__minute,self.__seconds))
    def __add__(self,other):
        print("\nTime1:","%.2d:%.2d:%.2d"%(self.__hour,self.__minute,self.__seconds))
        print("\nTime2:","%.2d:%.2d:%.2d"%(other.__hour,other.__minute,other.__seconds))
        
        self.__hour=self.__hour + other.__hour
        self.__minute=self.__minute + other.__minute
        self.__seconds=self.__seconds + other.__seconds
        return(self)
        

t1=Time(4,45,45)

t2=Time(6,55,60)

t3=(t1+t2)
print("\nTime1 + Time2:",t3.time(),"\n")