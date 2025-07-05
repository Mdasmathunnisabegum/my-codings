def i(num):
    print(f"we are in the function , before adding the num is{num}")
    num.append('asma')
    print(f"after adding the num  is {num}")
    
    
num=[1,2,3]
print(f"Now we are outside of the function where num is {num}")
i(num)
print(f"After calling the function the num is {num}")