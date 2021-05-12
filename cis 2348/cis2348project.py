# Joshua Jaja ID:1543343 Final Project Part 1 and 2

import csv
from datetime import datetime

class OutputInventory:
    #create output inventory files

    def __init__(self, item_list):
        self.item_list = item_list

    def full(self):
    #created csv output files for inventory by alphabet
        with open('C:\\Users\\Joshua Jaja\\Desktop\\FullInventory.csv', 'w') as file:
            items = self.item_list
        #ordered keys to write file based on manufacturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                m_name = items[item]['manufacturer']
                i_type = items[item]['item_type']
                price = items[item]['price']
                s_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id,m_name,i_type,price,s_date,damaged))

    def by_type(self):
    #csv output file by type
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'C:\\Users\\Joshua Jaja\\Desktop\\FullInventory.csv'
            with open('C:\\Users\\Joshua Jaja\\Desktop\\PhoneInventory.csv', 'w') as file:
                for item in keys:
                    id = item
                    m_name = items[item]['manufacturer']
                    price = items[item]['price']
                    s_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    i_type = items[item]['item_type']
                    if type == i_type:
                        file.write('{},{},{},{},{}\n'.format(id, m_name, price, s_date, damaged))

    def past_service(self):
    #created files past service date
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(), reverse=True)
        with open('C:\\Users\\Joshua Jaja\\Desktop\\TowerInventory.csv', 'w') as file:
            for item in keys:
                id = item
                m_name = items[item]['manufacturer']
                i_type = items[item]['item_type']
                price = items[item]['price']
                s_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(s_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, m_name, i_type, price, s_date, damaged))


    def damaged(self):
    #create damaged csv output file
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('C:\\Users\\Joshua Jaja\\Desktop\\DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                m_name = items[item]['manufacturer']
                i_type = items[item]['item_type']
                price = items[item]['price']
                s_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, m_name, i_type, price, s_date))


if __name__ == '__main__':
    items = {}
    files = ['C:\\Users\\Joshua Jaja\\Desktop\\ManufacturerList1.csv', 'C:\\Users\\Joshua Jaja\\Desktop\\PriceList1.csv', 'C:\\Users\\Joshua Jaja\\Desktop\\ServiceDatesList1.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    m_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = m_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    s_date = line[1]
                    items[item_id]['service_date'] = s_date

    inventory = OutputInventory(items)
# Create all the output files
    inventory.full()
    inventory.by_type()
    inventory.past_service()
    inventory.damaged()

    types = []
    manufacturers = []
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)

# Prompt the user for input
    u_input = None
    while u_input != 'q':
        u_input = input("\nPlease enter an item manufacturer and item type (ex: Apple laptop) or enter 'q' to quit:\n")
        if u_input == 'q':
            break
        else:
# Check word from user to see if there is a match in manufacturer and item type
            s_manufacturer = None
            s_type = None
            u_input = u_input.split()
            bad_input = False
            for word in u_input:
                if word in manufacturers:
                    if s_manufacturer:
                        bad_input = True
                    else:
                        s_manufacturer = word
                elif word in types:
                    if s_type:
                        bad_input = True
                    else:
                        s_type = word
        if not s_manufacturer or not s_type or bad_input:
            print("No such item in inventory")
        else:
            keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

            matching_items = []


            s_items = {}
            for item in keys:
                if items[item]['item_type'] == s_type:
                    today = datetime.now().date()
                    s_date = items[item]['service_date']
                    s_expiration = datetime.strptime(s_date, "%m/%d/%Y").date()
                    expired = s_expiration < today
                    if items[item]['manufacturer'] == s_manufacturer:
                        if not expired and not items[item]['damaged']:
                            matching_items.append((item, items[item]))
                    else:
                        if not expired and not items[item]['damaged']:
                            s_items[item] = items[item]

# item if matched
            if matching_items:
                item = matching_items[0]
                item_id = item[0]
                m_name = item[1]['manufacturer']
                i_type = item[1]['item_type']
                price = item[1]['price']
                print("Your item is: {}, {}, {}, {}\n".format(item_id, m_name, i_type, price))

#  closest in price to matched item
                if s_items:
                    m_price = price
                    c_item = None
                    closest_price_diff = None
                    for item in s_items:
                        if closest_price_diff == None:
                            c_item = s_items[item]
                            closest_price_diff = abs(int(m_price) - int(s_items[item]['price']))
                            item_id = item
                            m_name = s_items[item]['manufacturer']
                            i_type = s_items[item]['item_type']
                            price = s_items[item]['price']
                            continue
                        price_diff = abs(int(matched_price) - int(s_items[item]['price']))
                        if price_diff < closest_price_diff:
                            closest_item = item
                            closest_price_diff = price_diff
                            item_id = item
                            m_name = s_items[item]['manufacturer']
                            i_type = s_items[item]['item_type']
                            price = s_items[item]['price']
                    print("You may, also, consider: {}, {}, {}, {}\n".format(item_id, m_name, i_type, price))

            else:
                print("No such item in inventory")



