print("____To Count Odd and Even Numbers in the given list____\n")
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("\nThe List:",num)
even=0
odd=0
for i in num:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1

print("\nThe number of EVEN numbers in the list: ",even)
print("\nThe number of ODD numbers in the list: ",odd,"\n")
        

