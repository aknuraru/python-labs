def square_generator(N):
    for i in range(N + 1):
        yield i ** 2
N = int(input("Enter N: "))
for num in square_generator(N):
    print(num, end=" ")
