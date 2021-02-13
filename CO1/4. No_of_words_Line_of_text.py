counts = dict()
str='a good day is a good day, a bad day is a good story, at the end of the day, it is all good'
words = str.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)