print("_____SUM OF THE DIGITS OF A NUMBER___")
num=int(input("\nEnter any number with more than one digit: "))
n=str(num)

sum_of_digits = 0
for digit in n:
    sum_of_digits= sum_of_digits + int(digit)

print("Sum of the digits: ",sum_of_digits,"\n")