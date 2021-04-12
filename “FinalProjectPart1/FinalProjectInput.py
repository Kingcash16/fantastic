# Joshua Jaja ID:1543343 Final Project Part 1
import csv
from operator import itemgetter

mflists = []
prlist = []
sdlist = []


with open('C:\\Users\\Joshua Jaja\\Desktop\\ManufacturerList.csv') as manlist:
    ml = csv.reader(manlist)
for line in ml:
    mflists.append(line)

with open('C:\\Users\\Joshua Jaja\\Desktop\\PriceList.csv') as pricelist:
    pl = csv.reader(pricelist)
for line in pl:
    prlist.append(line)

with open('C:\\Users\\Joshua Jaja\\Desktop\\ServiceDatesList.csv') as sdlist:
    sl = csv.reader(sdlist)
for line in sl:
    sdl.append(line)


new_mflists = (sorted(mflists, key=itemgetter(0)))
new_prlist = (sorted(prlist, key=itemgetter(0)))
new_sdlist = (sorted(sdlist, key=itemgetter(0)))


for x in range(0, len(new_mflists)):
    new_mflists[x].append(prl[x][1])

for x in range(0, len(new_mflists)):
    new_mflists[x].append(sdl[x][1])

final_list = new_mflists

full_inventory = (sorted(final_list, key=itemgetter(1)))


with open('C:\\Users\\Joshua Jaja\\Desktop\\FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)

for x in range(0, len(full_inventory)):
    fiwrite.writerow(full_inventory[x])


item_type = final_list
tower_list = []
laptop_list = []
psd_list = []
phone_list = []


for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower_list.append(item_type[x])
    elif item_type[x][2] == "phone":
     phone_list.append(item_type[x])
    elif item_type[x][2] == "laptop":
     laptop_list.append(item_type[x])
    elif item_type[x][2] == "psd":
     psd_list.append(item_type[x])

with open('C:\\Users\\Joshua Jaja\\Desktop\\LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)

for x in range(0, len(laptop_list)):
    liwrite.writerow(laptop_list[x])

with open('C:\\Users\\Joshua Jaja\\Desktop\\PastServiceDateInventory.csv', 'w') as newfile:
    pswrite = csv.writer(newfile)

for x in range(0, len(psd_list)):
    pswrite.writerow(psd_list[x])

with open('C:\\Users\\Joshua Jaja\\Desktop\\PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)

for x in range(0, len(phone_list)):
    piwrite.writerow(phone_list[x])

with open('C:\\Users\\Joshua Jaja\\Desktop\\TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)

for x in range(0, len(tower_list)):
    tiwrite.writerow(tower_list[x])



dlist = []

for x in range(0, len(item_type)):
    if item_type[x][3] == "damaged":
        dlist.append(item_type[x])

dlist = (sorted(dlist, key=itemgetter(4), reverse=True))


with open('C:\\Users\\Joshua Jaja\\Desktop\\DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)

for x in range(0, len(dlist)):
    diwrite.writerow(dlist[x])

user_manuf = str(input("Enter  manufacturer: "))

user_type = str(input("Please enter  item type: "))

your_item = []



while (user_manuf != "q"):
    for x in range(0, len(final_list)):
     if user_manuf in final_list[x] and user_type in final_list[x]:
        your_item.append(final_list[x])


if len(your_item) != 0:
   your_item = sorted(your_item, key=itemgetter(4), reverse=True)
   print("Your Item is: ", your_item[0])
else:
    print("No item in Inventory")
user_manuf = str(input("Enter manufacturer, or q to exit query:"))

user_type = str(input("Please enter item type: "))