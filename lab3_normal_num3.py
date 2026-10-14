class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_cart(self):
        total = 0
        for product in self.products:
            print(product.name, "-", product.price, "руб.")
            total += product.price
        print("Итого:", total, "руб.")


product1 = Product("Хлеб", 50)
product2 = Product("Молоко", 100)
product3 = Product("Сыр", 200)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.show_cart()