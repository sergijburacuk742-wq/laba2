def format_price(price):
    return f"ціна: {price:.2f} грн"

def check_availability(*products):
    store_inventory = {
        'bread': True,
        'milk': True,
        'aggs': False,
        'cheese': True,
        'sausage': False,
        'butter': True
    }
    result = {}
    for product in products:
        result[product] = store_inventory.get(product, False)  # Якщо нема в магазині — False
    return result

def process_order():
    # Словник цін на товари
    product_prices = {
        'bread': 20.5,
        'milk': 30.0,
        'aggs': 40.75,
        'cheese': 85.0,
        'sausage': 120.0,
        'butter': 55.5
    }

    # Отримати замовлення
    order = input("Введіть замовлення (товари через кому): ").lower().split(',')
    order = [item.strip() for item in order]  # Прибираємо зайві пробіли

    availability = check_availability(*order)

    if all(availability.values()):
        print("Усі товари в наявності.")
        print("Що ви хочете зробити?")
        print("1 - Переглянути ціну")
        print("2 - Купити")

        choice = input("Ваш вибір: ")

        if choice == '1':
            total = sum(product_prices[item] for item in order)
            print(format_price(total))

        elif choice == '2':
            total = sum(product_prices[item] for item in order)
            print(f"Ви купили: {', '.join(order)}")
            print(f"До сплати — {format_price(total)}")
        else:
            print("Невірний вибір. Спробуйте ще раз.")
    else:
        print("Деякі товари відсутні:")
        for item, is_available in availability.items():
            if not is_available:
                print(f"- {item}")
        print("Замовлення неможливе.")

def main():
    while True:
        print("\nМеню:")
        print("1 - Зробити замовлення")
        print("2 - Вийти")
        option = input("Ваш вибір: ")

        if option == '1':
            process_order()
        elif option == '2':
            print("Дякуємо за відвідування!")
            break
        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()