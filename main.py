class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def info(self):
        print(f"Магазин {self.name} расположен по адресу: {self.address}.")
        print("Ассортимент:")
        for item, price in self.items.items():
            print(f"{item}: {price}")

# Создание экземпляров магазинов
store1 = Store("Продукты", "ул. Ленина 1")
store2 = Store("Перекресток", "ул. Мира 2")
store3 = Store("Дикси", "ул. Солнечная 3")

# Добавление товаров в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.info()

store2.add_item("вода", 0.9)
store2.add_item("масло", 1.2)
store2.info()

store3.add_item("молоко", 1.0)
store3.add_item("хлеб", 2.0)
store3.info()

# Тестирование методов на одном из магазинов
store1.add_item("шоколад", 1.5)
print("Цена шоколада:", store1.get_price("шоколад"))
store1.update_price("шоколад", 1.75)
store1.remove_item("яблоки")
print("Цена яблок:", store1.get_price("яблоки"))
store1.info()
store2.info()
store3.info()
