# Joshua Jaja ID:1543343 Zylab 11.27
t_dict={}
i=1
count=1
for i in range(1,6):
    j_num = int(input('Enter player {}\'s jersey number:\n' .format(i)))
    r = int(input('Enter player {}\'s rating:\n' .format(i)))
    print()
    if j_num < 0 and j_num > 99 and r < 0 and r > 9:
        print('invalid entry')
        break
    else:
        t_dict[j_num] = r
print("ROSTER")
for j_num,r in sorted(t_dict.items()):
    print("Jersey number: %d, Rating: %d" % (j_num,r))
option=''
while option.upper()!='Q':
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'
          'r - Output players above a rating\no - Output roster\nq - Quit\n')
    option = input('Choose an option:\n')
    if option == 'a':
        j_num = int(input('Enter a new player\'s jersey number:\n' .format(i)))
        r = int(input('Enter the players\'s rating:\n'.format(i)))
        t_dict[j_num] = r
    elif option == 'd':
        j_num = int(input('Enter a jersey number:\n'))
        if j_num in t_dict.keys():
            del t_dict[j_num]
    elif option == 'u':
        j_num = int(input('Enter a jersey number:\n'))
        if j_num in team_dict.keys():
            r = int(input('Enter a new rating for player:\n'))
            t_dict[j_num] = r
    elif option == 'r':
        r_input=int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(r_input))
        for j_num,r in sorted(t_dict.items()):
            if r > r_input:
                print("Jersey number: %d, Rating: %d" % (j_num,r))
    elif option == 'o':
        print("ROSTER")
        for j_num,r in sorted(t_dict.items()):
            print("Jersey number: %d, Rating: %d" % (j_num,r))

