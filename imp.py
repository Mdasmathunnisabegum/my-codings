n = input()
print(f"Lenght is {len(n)}")
l = []
for i in range(len(n)):
    l.append(n[i])
    
l = l[::-1]
print("Rev:")
for i in range(len(n)):
    print(l[i])