import numpy as np

def encode(a , b):
    x = 0.5*(a**2 + b**2 + a + 2*a*b + 3*b)
    return x
def decode (x):
    r = np.floor((2*x + 0.25)**(0.5) - 0.5)
    b = x - 0.5*(r**2 + r)
    a = r - b
    return a , b

def stack_encode(ls):
  
    cond_one = any(n <= 0 for n in ls)
    cond_two = not isinstance(ls,list)
    cond_three = any(not isinstance(n,int) <= 0 for n in ls)
    if cond_one  or cond_two or cond_three:
        raise Exception("the list contain 0 or/and negative number")
        
    stack_encode = 0
    ls = [0] + ls
    for m,n in zip(ls[:-1],ls[1:]) :
        if stack_encode == 0:
            stack_encode = encode(m , n)
        else:
            stack_encode = encode(stack_encode, n)
    return stack_encode

def stack_decode(x):
    stack_output = []
    a = 1
    while a != 0 :
        a,b = decode(x)
        stack_output.append(b)
        x = a
    stack_output.append(x)
    return stack_output[::-1][1:]
        
if __name__ == "__main__"

    aa , bb = 55564 , 888      
    print(encode(aa,bb) , decode(encode(aa,bb)))

    ls = [ 1 , 10 , 8 , 122, 10]
    print(stack_encode(ls))
    print(stack_decode(stack_encode(ls)))
