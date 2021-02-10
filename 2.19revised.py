# Joshua Jaja ID:1543343 Zylab 2.19
L_juice = float(input('Enter amount of lemon juice (in cups):'))
Water = float(input('Enter amount of water (in cups):'))
a_nectar = float (input('Enter amount of a nectar (in cups):'))
serves = float(input('How many serves does this make '))

print("")
print('Lemonade ingredients- yields '+str('{:.2f}'.format(serves))+'servings')
print(str('{:.2f}'.format(L_juice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(Water))+' cups(s) water')
print(str('{:.2f}'.format(a_nectar))+' cup(s) a nectar')

n_serve = float(input('How many servings would you to make?'))
x = n_serve/serves
n_l_juice = L_juice*x
n_water = Water*x
n_a_nectar = a_nectar*x

print("")
print('Lemonade ingredients- yields '+str('{:.2f}'.format(serves))+'servings')
print(str('{:.2f}'.format(L_juice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(Water))+' cups(s) water')
print(str('{:.2f}'.format(a_nectar))+' cup(s) a nectar')

print('Lemonade ingredients - yields '+str('{:.2f}'.format(serves))+'serves')
print(str('{:.2f}'.format(n_l_juice/16))+'cups(s) lemon juice')
print(str('{:.2f}'.format(n_water/16))+'cups(s) water')
print(str('{:.2f}'.format(n_a_nectar/16))+'cups(s) a nectar')





