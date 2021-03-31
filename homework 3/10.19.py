class ItemToPurchase:
    def __init__(self, i_n='none', i_p=0, i_q=0, item_description='none'):
        self.i_n = i_n
        self.i_p = i_p
        self.i_q = i_q
        self.item_description = item_description
    def print_item_c(self):
        string = '{} {} @ ${} = ${}'.format(self.i_n, self.i_q, self.i_p,                                            (self.i_q * self.i_p))
        cost = self.i_q * self.i_p
        return string, cost
    def print_item_description(self):
        string = '{}: {}, %d oz.'.format(self.i_n, self.item_description, self.i_q)
        print(string)
        return string
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    def add_item(self):
        print('ADD ITEM TO CART')
        i_n = str(input('Enter the item name:'))
        print()
        i_d = str(input('Enter the item description:'))
        print()
        i_p = int(input('Enter the item price:'))
        print()
        i_q = int(input('Enter the item quantity:'))
        print()
        self.cart_items.append(ItemToPurchase(i_n, i_p, i_q, i_d))
    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        string = str(input('Enter name of item to remove:'))
        print()
        i = 0
        for item in self.cart_items:
            if (item.i_n == string):
                del self.cart_items[i]
                flag = True
                break
            else:
                flag = False
            i += 1
        if (flag == False):
            print('Item not found in cart. Nothing removed.')
    def modify_item(self):
        print('CHANGE ITEM QUANTITY')
        n = str(input('Enter the item name:'))
        print()
        for item in self.cart_items:
            if (item.i_n == n):
                quantity = int(input('Enter the new quantity:'))
                print()
                item.i_q = quantity
                flag = True
                break
            else:
                flag = False
        if (flag == False):
            print('Item not found in cart. Nothing modified.')
        print()
    def get_num_items_in_cart(self):
        n_items = 0
        for item in self.cart_items:
            n_items = n_items + item.i_q
        return n_items
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.i_q * item.i_p)
            total_cost += cost
        return total_cost
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()
    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.i_n, item.i_d))
    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        print()
        tc = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.i_n, item.i_q,item.i_p, (item.i_q * item.i_p)))
            tc += (item.i_q * item.i_p)
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print()
        print('Total: ${}'.format(tc))
def print_menu(customer_C):
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')
    command = ''
    while (command != 'q'):
        print(menu)
        command = input('Choose an option:')
        print()
        while (command != 'a' and command != 'o' and command != 'i' and command != 'r'
               and command != 'c' and command != 'q'):
            command = input('Choose an option:')
            print()
        if (command == 'a'):
            customer_C.add_item()
        if (command == 'o'):
            customer_C.output_cart()
        if (command == 'i'):
            customer_C.print_descriptions()
        if (command == 'r'):
            customer_C.remove_item()
        if (command == 'c'):
            customer_C.modify_item()
def main():
    customer_name = str(input('Enter customer\'s name:'))
    print()
    current_date = str(input('Enter today\'s date:'))
    print('\n')
    print('Customer name:', customer_name, end='\n')
    print('Today\'s date:', current_date, end='\n')
    nc = ShoppingCart(customer_name, current_date)
    print_menu(nc)
if __name__ == '__main__':
    main()