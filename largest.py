l=[3,2,1,5,2]
largest=l[0]
for i in range(0,len(l)):
    if l[i] > largest:
        largest = l[i]
print(largest)