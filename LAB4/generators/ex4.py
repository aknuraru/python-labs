def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a, b = map(int, input("Enter a and b: ").split())
for sq in squares(a, b):
    print(sq)
