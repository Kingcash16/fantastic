# Joshua Jaja ID:1543343 Zylab 11.18
ig = input().split()
n_n_int=[]
for number in ig:
    number = int(number)
    if number >= 0:
        n_n_int.append(number)
n_n_int.sort()
for i in n_n_int:
    print(i,end=' ')