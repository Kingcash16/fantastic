# Joshua Jaja ID:1543343 Zylab 10.11
class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
    def g_calories(self, n_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * n_servings;
        return calories
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
if __name__ == "__main__":
    f_item1 = FoodItem()
    i_name = input()
    a_fat = float(input())
    a_carbs = float(input())
    a_protein = float(input())
    f_item2 = FoodItem(i_name, a_fat, a_carbs, a_protein)
    n_servings = float(input())
    f_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(n_servings, f_item1.g_calories(n_servings)))
    print()
    f_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(n_servings, f_item2.g_calories(n_servings)))