#Joshua Jaja ID:1543343 Zylab 12.9
p = input().split()
n = p[0]
while n != '-1':
    try:
        a = int(p[1]) + 1
    except Exception as ex:
        a = 0
    print('{} {}'.format(n, a))
    p = input().split()
    n = p[0]