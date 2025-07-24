a=[4,5,6,7,8,9]
temp=a[0]
for i in range(1,len(a)):
    a[i-1]=a[i]
a[-1]=temp
print(a)