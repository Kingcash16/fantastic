# Joshua Jaja ID:1543343 Zylab 8.10:

w = input()
a= w.replace('','')
low = 0
high = len(a)-1
flag = False
while (high>low):
    if (a[low]!=a[high]):
        flag = True
        break
    low+=1
    high-=1
if (flag):
    print(w,"is not a palindrome")
else:
    print(w,"is a palindrome")

