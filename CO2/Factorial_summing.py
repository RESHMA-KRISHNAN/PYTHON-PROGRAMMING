def factorial(n):
    if n==0:
        return 1
    else:
        fact = factorial(n-1)
        fact_1 = n*fact
        return fact_1
sum=0 
limit=int(input("Please enter the limit: "))
for n in range(limit):
    if n%2 !=0:
        result=n/(factorial(n))
        sum+=result

print("\nThe value of 1 + 3/3! + 5/5! +.....+",limit,"/",limit,"! is: ",sum,"\n")