# Joshua Jaja ID:1543343 Zylab 10.17
class ItemToPurchase:
  def __init__(self):
   self.item_name = "none"
   self.item_price = 0.0
   self.item_quantity = 0
def print_item_cost(self):
    print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
    self.item_price * self.item_quantity))
if __name__ == "__main__":
    print("Item 1")
    i1 = ItemToPurchase()
    i1.item_name = input("Enter the item name:\n")
    i1.item_price = int(input("Enter the item price:\n"))
    i1.item_quantity = int(input("Enter the item quantity:\n"))
    print("\nItem 2")
    i2 = ItemToPurchase()
    i2.item_name = input("Enter the item name:\n")
    i2.item_price = int(input("Enter the item price:\n"))
    i2.item_quantity = int(input("Enter the item quantity:\n"))
    t_c = i1.item_price * i1.item_quantity + i2.item_price * i2.item_quantity
    print("\nTOTAL COST")
    i1.print_item_cost()
    i2.print_item_cost()
    print("\nTotal: $" + str(t_c))