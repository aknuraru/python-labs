def permutations(some):
    n = len(some)

    for i in range(n):
        for j in range(n):
            print(some[(j-i)], end=" ")
        print()
k=str(input("soz:"))
permutations(k)

"""
import itertools

def permutations(s):
    for perm in itertools.permutations(s):
        print("".join(perm))
k = input("Enter a string: ")
permutations(k)
"""