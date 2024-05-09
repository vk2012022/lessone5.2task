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

# Создание экземпляров магазинов
store1 = Store("Магазин A", "ул. Ленина 1")
store2 = Store("Магазин B", "ул. Мира 2")
store3 = Store("Магазин C", "ул. Солнечная 3")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("water", 0.9)
store2.add_item("bread", 1.2)

store3.add_item("milk", 1.0)
store3.add_item("eggs", 2.0)

# Тестирование методов на одном из магазинов
store1.add_item("chocolate", 1.5)
print("Цена шоколада:", store1.get_price("chocolate"))
store1.update_price("chocolate", 1.75)
store1.remove_item("apples")
print("Цена яблок:", store1.get_price("apples"))
