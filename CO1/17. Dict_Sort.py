import operator
print("\n__________SORTING OF DICTIONARY__________")
data={'Reshma':87,'Arya':85,'Anjali':90,'Sreelekshmi':78,'Subina':79}
print("\nOriginal Dictionary:",data)
sorted_asc = dict(sorted(data.items(),key=operator.itemgetter(1)))
sorted_desc = dict(sorted(data.items(),key=operator.itemgetter(1), reverse=True))
print("\nSorted in ascending order by value:\n",sorted_asc)
print("\nSorted in descending order by value:\n",sorted_desc)
print("\n")