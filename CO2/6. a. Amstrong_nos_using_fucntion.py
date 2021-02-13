def amstrong(num): 
    sum = 0  
    temp = num  
    while temp > 0:
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
    
    if num == sum:
        print(num)

print("\nThe amstrong numbers between 1 and 500 are: ")
for i in range(1,501):
    amstrong(i)

