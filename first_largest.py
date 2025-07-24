arr=[4,5,6,78,8,9]
largest = arr[0]
for i in range(0,len(arr)):
    if arr[i] > largest:
        largest=arr[i]
print(largest)

