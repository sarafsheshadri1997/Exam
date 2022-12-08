def add(a, b):  
    sum = a + b  
    print(a, "+", b, "=", sum)  
  
# defining subtraction function  
def subtract(a, b):  
    difference = a - b  
    print(a, "-", b, "=", difference)  
  
# defining multiplication function  
def multiply(a, b):  
    product = a * b  
    print(a, "x", b, "=", product)  
  

time = 12.00
rate = 15
principle=time*rate

# Calcualtion
simple_interest = (time*rate)/100
compound_interest = ( (1+rate/100)**time - 1)

# Displaying result
print('Simple interest is: %f' % (simple_interest))
print('Compound interest is: %f' %(compound_interest))