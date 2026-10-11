calc_method = input("Which mathematical process will you be using today? (add, sub, multiply, divide): ")

if calc_method == 'add':
    p = float(input('p=? '))
    q = float(input('q=? '))

    def add(p, q):
        return p + q

    print(add(p, q))

elif calc_method == "sub":
    p = float(input('p=? '))
    q = float(input('q=? '))

    def sub(p, q):
        return p - q

    print(sub(p, q))

elif calc_method == 'multiply':
    p = float(input('p=? '))
    q = float(input('q=? '))

    def multiply(p, q):
        return p * q

    print(multiply(p, q))

elif calc_method == 'divide':
    p = float(input('p=? '))
    q = float(input('q=? '))

    def divide(p, q):
        if q == 0:
            print("Cannot divide by zero.")
            return
        return p / q

    print(divide(p, q))

else:
    print("Invalid operation.")