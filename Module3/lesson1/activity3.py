calc_method = str(input("Which mathematical process will you be using today? (add, sub, multiply, divide): "))

if calc_method == 'add':
    p=str(input('p=? '))
    q=str(input('q=? '))
    def add(p,q):
        return p + q
add()    

if calc_method == "sub":
    p=str(input('p=? '))
    q=str(input('q=? '))
    def sub(p,q):
        return p - q
sub()

if calc_method =='multiply':
    p=str(input('p=? '))
    q=str(input('q=? '))
    def multiply(p,q):
        return p * q
multiply()

if calc_method =='divide':
    p=str(input('p=? '))
    q=str(input('q=? '))
    def divide(p,q):
        return p / q
divide()