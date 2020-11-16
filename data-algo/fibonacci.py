
def fibonacci_iterative(n):
    
    # store value
    nex = 0

    current = 1
    # loop n number times
    i  = 1
    ls = []
    while i <=  n + 1:
        ls.append(nex)
        ls.append(current)
        nex = nex + current
      
        current = current + nex
        i += 2
    ls.append(nex)
   
   
    #keep adding to value 
    return ls[n]

def fibonacci_recursive(n):
    if n < 2:
        return n 

    return fibonacci_recursive(n - 1 ) + fibonacci_recursive(n -2)


print(fibonacci_iterative(3))
print(fibonacci_iterative(6))
print(fibonacci_iterative(7))
print(fibonacci_iterative(8))

print(fibonacci_recursive(3))
print(fibonacci_recursive(6))
print(fibonacci_recursive(7))
print(fibonacci_recursive(8))