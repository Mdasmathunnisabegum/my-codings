l=[1,2,4,5]
size=len(l)
for i in range(1,size+2):
    if i not in l:
        print(f"missing num is:{i}")