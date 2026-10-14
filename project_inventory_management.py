import math

products = [
    {"code": 10, "name": "rice", "price": 24.90, "quantity": 10}
]

def read_number(prompt: str, number_type: type, allow_negative: bool = False):
    raw_value = input(prompt).strip().replace(",", ".")
    try:
        value = number_type(raw_value)
    except ValueError:
        print("Invalid value or empty field. Please try again.")
        return None
    if isinstance(value, float) and not math.isfinite(value):
        print("Invalid value. Please try again.")
        return None
    if not allow_negative and value < 0:
        print("Negative values are not allowed. Please try again.")
        return None
    return value

def register_product(products: list) -> None:
    code = read_number("Enter the product code you want to register (numbers only): ", int)
    if code is None:
        return
    for product in products:
        if product["code"] == code:
            print("Product already registered.")
            return

    name = input("Enter the product name you want to register: ").strip().lower()
    if not name:
        print("This field cannot be empty. Please try again.")
        return
    price = read_number("Enter the product price in reais (numbers only): ", float)
    if price is None:
        return
    quantity = read_number("Enter the quantity to register (numbers only): ", int)
    if quantity is None:
        return

    products.append({
        "code": code,
        "name": name,
        "price": price,
        "quantity": quantity,
    })
    print(f"Product '{name}' registered successfully!")

def calculate_total_units(products: list) -> int:
    return sum(product["quantity"] for product in products)

while True:
    print("\nOption 1 -> Register a product.")
    print("Option 2 -> Calculate total units in stock.")
    print("Option 3 -> Exit.")
    option = input("Enter the desired option: ").strip()
    if option == "1":
        register_product(products)
    elif option == "2":
        total_units = calculate_total_units(products)
        print(f"The total quantity is {total_units} units.")
    elif option == "3":
        break
    else:
        print("Invalid option. Please try again.")