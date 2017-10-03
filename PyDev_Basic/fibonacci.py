'''
Created on 5 de set de 2017

@author: luiz
'''
# Python 3: Fibonacci series up to n
def fibonacci(n):
    a, b = 0, 1
    print(a)
    print(b)
    print()
    
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

