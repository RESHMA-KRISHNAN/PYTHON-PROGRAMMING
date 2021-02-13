print("\n____To enlist the numbers between 1000 and 2000 which are divisible by 7 and are multiples of 5_____\n")
l=[]
for i in range(1000,2001):
    if i%7==0 and i%5==0:
        l.append(i)
print("The required output is: ",l,"\n")
