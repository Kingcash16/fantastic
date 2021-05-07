# Joshua Jaja ID:1543343 Final Project Part 1

import csv
from operator import itemgetter

mfls = []
prls = []
sdls = []

with open('C:\\Users\\Joshua Jaja\\Desktop\\ManufacturerList1.csv') as manlists:
    ml = csv.reader(manlists)
    for line in ml:
        mfls.append(line)

with open('C:\\Users\\Joshua Jaja\\Desktop\\PriceList1.csv') as pricelists:
    pl = csv.reader(pricelists)
    for line in pl:
        prls.append(line)

with open('C:\\Users\\Joshua Jaja\\Desktop\\ServiceDatesList1.csv') as sdlists:
    sl = csv.reader(sdlists)
    for line in sl:
        sdls.append(line)

new_mfls = (sorted(mfls, key=itemgetter(0)))
new_prls = (sorted(prls, key=itemgetter(0)))
new_sdls = (sorted(sdls, key=itemgetter(0)))

for x in range(0, len(new_mfls)):
    new_mfls[x].append(prls[x][1])

for x in range(0, len(new_mfls)):
    new_mfls[x].append(sdls[x][1])

final_lists = new_mfls

full_inventory = (sorted(final_lists, key=itemgetter(1)))

with open('C:\\Users\\Joshua Jaja\\Desktop\\FullInventory1.csv', 'w') as newfile:
    fwrite = csv.writer(newfile)

    for x in range(0, len(full_inventory)):
        fwrite.writerow(full_inventory[x])

item_type = final_lists
tower_list = []
laptop_list = []
phone_list = []
psd_list = []

for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower_list.append(item_type[x])
    elif item_type[x][2] == "phone":
        phone_list.append(item_type[x])
    elif item_type[x][2] == "laptop":
        laptop_list.append(item_type[x])

with open('C:\\Users\\Joshua Jaja\\Desktop\\LaptopInventory1.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)

    for x in range(0, len(laptop_list)):
        liwrite.writerow(laptop_list[x])
with open('C:\\Users\\Joshua Jaja\\Desktop\\PastServiceDateInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)

    for x in range(0, len(psd_list)):
        liwrite.writerow(psd_list[x])

with open('C:\\Users\\Joshua Jaja\\Desktop\\PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)

    for x in range(0, len(phone_list)):
        piwrite.writerow(phone_list[x])

with open('C:\\Users\\Joshua Jaja\\Desktop\\TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)

    for x in range(0, len(tower_list)):
        tiwrite.writerow(tower_list[x])

damagedlist = []

for x in range(0, len(item_type)):
    if item_type[x][3] == "damaged":
        damagedlist.append(item_type[x])

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

with open('C:\\Users\\Joshua Jaja\\Desktop\\DamagedInventory1.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)

    for x in range(0, len(damagedlist)):
        diwrite.writerow(damagedlist[x])