from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self, file_name='products.txt'):
        self.file_name = file_name

    def get_products(self):
        with open(self.file_name, 'r') as file:
            pprint(file.read())

    def add(self, *products):
        for product in products:
            p_str = str(product)
            with open(self.file_name, 'r') as file:
                file_contents = file.read()
            if p_str in file_contents:
                print(f'Продукт {p_str} уже есть в магазине')
            else:
                with open(self.file_name, 'a') as file:
                    file.write(f'{p_str}\n')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # выводим __str__
s1.add(p1, p2, p3)
s1.get_products()
