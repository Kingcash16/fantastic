#Joshua Jaja ID:1543343 Zylab 6.17:

pd = input()
pd = list(pd)

for i in range(0, len(pd)):
    if pd[i] == 'i':
        pd[i] = '!'
    elif pd[i] == 'a':
        pd[i] = '@'
    elif pd[i] == 'm':
        pd[i] = 'M'
    elif pd[i] == 'B':
        pd[i] = '8'
    elif pd[i] == 'o':
        pd[i] = '.'

st_pw = ""
st_pw = st_pw.join(pd)

st_pw = st_pw + "q*s"

print(st_pw)

