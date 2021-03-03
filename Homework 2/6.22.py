# Joshua Jaja ID:1543343 Zylab 6.22:

j = int(input())
k = int(input())
L = int(input())

m = int(input())
n = int(input())
o = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if x * j + y * k == L and x * m + n * y == o:
            print(x, y)
            solution_found = True
if not solution_found:
    print("No solution")

