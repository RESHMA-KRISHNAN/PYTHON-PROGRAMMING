a=int(input("Enter range from:"))
z=int(input("Enter range to:"))
for i in range(a,z+1):
    for j in range(32,100):
        if j*j==i:
           string= str(i)
           if int(string[0])%2 == 0 and int(string[1])%2 == 0 and int(string[2])%2 == 0 and int(string[3])%2 == 0:
               print(i)
           