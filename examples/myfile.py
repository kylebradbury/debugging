def myfunc(A):
    # Create a copy of the list and square all of it's entries
    B = A
    for i,b in enumerate(B):
        B[i] = b**2
    
    # Sum up the entries of each list and return them
    return [sum(A), sum(B)]

mylist = [1,2,3]

result = myfunc(mylist)
print(result)