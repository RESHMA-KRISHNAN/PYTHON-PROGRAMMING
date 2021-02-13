n=int(input("Enter the series limit: "))
first=0      
second=1                                   
if n<=0:
    print("The requested series is",first)
else:
    print(first,second,end=" ")
    for x in range(2,n):
        next=first+second                           
        print(next,end=" ")
        first=second
        second=next