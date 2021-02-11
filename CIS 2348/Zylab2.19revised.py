#Joshua Jaja ID 1543343
l_juice_cup = float(input('Enter amount of lemon juice (in cups):\n'))
w_cup = float(input('Enter amount of water (in cups):\n'))
n_cup = float(input('Enter amount of agave nectar (in cups):\n'))
no_of_serves = float(input('How many servings does this make?\n'))
print('\nLemonade ingredients - yields', "{:.2f}".format(no_of_serves), 'servings')
print("{:.2f}".format(l_juice_cup), 'cup(s) lemon juice')
print("{:.2f}".format(w_cup), 'cup(s) water')
print("{:.2f}".format(n_cup), 'cup(s) agave nectar\n')


d_serve = float(input('How many servings would you like to make?\n'))
print('\nLemonade ingredients - yields',"{:.2f}".format(d_serve), 'servings')
serving = d_serve / no_of_serves
l_juice_cup = l_juice_cup * serving
w_cup = w_cup * serving
n_cup = n_cup * serving

print("{:.2f}".format(l_juice_cup), 'cup(s) lemon juice')
print("{:.2f}".format(w_cup), 'cup(s) water')
print("{:.2f}".format(n_cup), 'cup(s) agave nectar\n')



print('Lemonade ingredients - yields', "{:.2f}".format(d_serve), 'servings')
l_G = l_juice_cup / 16
w_G = w_cup / 16
a_G = n_cup / 16

print("{:.2f}".format(l_G), 'gallon(s) lemon juice')
print("{:.2f}".format(w_G), 'gallon(s) water')
print("{:.2f}".format(a_G), 'gallon(s) agave nectar')











