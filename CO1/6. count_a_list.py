print('\nTo store a list of first names. Count the occurrences of ‘a’ within the list.\n')
l=['arya','reshma','rajath','anamika','ananya']
i=0
count=0
while i<len(l):
  count=count+l[i].count('a')
  i=i+1
print('\nList of names:\n',l)
print('\nNo. of "a" within the list: ',count,'\n')