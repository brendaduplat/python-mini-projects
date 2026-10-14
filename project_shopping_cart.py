import unicodedata

def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore")
    text = text.decode("ascii")
    return text

def calculate_discount(price):
    if price > 500:
        return 0.20
    if price > 200:
        return 0.10
    return 0.0

store = [
    {"product": "Gaming Mouse", "price": 89.90},
    {"product": "Mechanical Keyboard", "price": 249.90},
    {"product": "Headset", "price": 179.90},
    {"product": "Full HD Webcam", "price": 129.90},
    {"product": "24-inch Monitor", "price": 899.90},
    {"product": "SSD 500GB", "price": 299.90},
    {"product": "External HD 1TB", "price": 379.90},
    {"product": "64GB Flash Drive", "price": 49.90},
    {"product": "Wi-Fi Router", "price": 219.90},
    {"product": "Office Chair", "price": 749.90},
    {"product": "Bluetooth Speaker", "price": 159.90},
    {"product": "USB Microphone", "price": 329.90},
    {"product": "Smartwatch", "price": 599.90},
    {"product": "Portable Charger", "price": 99.90},
    {"product": "LED Lamp", "price": 79.90},
    {"product": "Laptop Stand", "price": 69.90},
    {"product": "USB Hub", "price": 59.90},
    {"product": "Numeric Keypad", "price": 119.90},
    {"product": "Bluetooth Controller", "price": 289.90},
    {"product": "Drawing Tablet", "price": 949.90},
]

cart = []
while True:
    user_input = input("Enter the product name to add to the cart, or 'checkout' to proceed to payment: ")
    search = normalize(user_input.strip())
    if search == "checkout":
        break
    added = False
    for item in store:
        if search == normalize(item["product"]):
            cart.append(item.copy())
            added = True
            break
    if added:
        print("Product added successfully.")
    else:
        print("Product not found.")

for item in cart:
    discount = calculate_discount(item["price"])
    item["discount"] = discount
    item["final_price"] = round(item["price"] * (1 - discount), 2)

if cart:
    for item in cart:
        print(
            f"Product: {item['product']}; "
            f"Gross price: R$ {item['price']:.2f}; "
            f"Discount: {item['discount']:.0%}; "
            f"Final price: R$ {item['final_price']:.2f}"
        )
    total = sum(item["final_price"] for item in cart)
    print(f"The total value of your purchase is R$ {total:.2f}")
else:
    print("Empty cart.")