sales = [
    {"product": "Dell Laptop", "category": "Computers", "value": 4500, "month": "January"},
    {"product": "Logitech Mouse", "category": "Computers", "value": 120, "month": "January"},
    {"product": "Dell Laptop", "category": "Computers", "value": 4500, "month": "February"},
    {"product": "Redragon Mechanical Keyboard", "category": "Computers", "value": 280, "month": "February"},
    {"product": "Logitech Mouse", "category": "Computers", "value": 120, "month": "March"},

    {"product": "Samsung Smartphone", "category": "Electronics", "value": 2200, "month": "January"},
    {"product": "Xiaomi Smartwatch", "category": "Electronics", "value": 600, "month": "January"},
    {"product": "Samsung Smartphone", "category": "Electronics", "value": 2200, "month": "February"},
    {"product": "JBL Bluetooth Headphones", "category": "Electronics", "value": 250, "month": "March"},
    {"product": "Samsung Smartphone", "category": "Electronics", "value": 2200, "month": "April"},

    {"product": "Brastemp Refrigerator", "category": "Home Appliances", "value": 3200, "month": "January"},
    {"product": "Mondial Air Fryer", "category": "Home Appliances", "value": 450, "month": "February"},
    {"product": "Electrolux Microwave", "category": "Home Appliances", "value": 700, "month": "March"},
    {"product": "Mondial Air Fryer", "category": "Home Appliances", "value": 450, "month": "April"},
    {"product": "Brastemp Refrigerator", "category": "Home Appliances", "value": 3200, "month": "May"},

    {"product": "Basic T-Shirt", "category": "Clothing", "value": 80, "month": "January"},
    {"product": "Jeans", "category": "Clothing", "value": 180, "month": "February"},
    {"product": "Nike Sneakers", "category": "Clothing", "value": 450, "month": "March"},
    {"product": "Basic T-Shirt", "category": "Clothing", "value": 80, "month": "April"},
    {"product": "Nike Sneakers", "category": "Clothing", "value": 450, "month": "May"},

    {"product": "Python Book", "category": "Books", "value": 100, "month": "January"},
    {"product": "SQL Book", "category": "Books", "value": 90, "month": "February"},
    {"product": "Python Book", "category": "Books", "value": 100, "month": "March"},
    {"product": "Data Science Book", "category": "Books", "value": 150, "month": "April"},
    {"product": "Python Book", "category": "Books", "value": 100, "month": "May"},
]

revenue_by_category = {}
revenue_by_month = {}
for sale in sales:
    category = sale["category"]
    month = sale["month"]
    value = sale["value"]
    revenue_by_category[category] = revenue_by_category.get(category, 0) + value
    revenue_by_month[month] = revenue_by_month.get(month, 0) + value

top_revenue_month = max(revenue_by_month, key=revenue_by_month.get)

revenue_by_product_in_category = {}
for sale in sales:
    category = sale["category"]
    product = sale["product"]
    if category not in revenue_by_product_in_category:
        revenue_by_product_in_category[category] = {}
    revenue_by_product_in_category[category][product] = (
        revenue_by_product_in_category[category].get(product, 0) + sale["value"]
    )

top_product_by_category = {}
for category, products in revenue_by_product_in_category.items():
    top_product_by_category[category] = max(products, key=products.get)

print("Revenue by category:")
for category, total in revenue_by_category.items():
    print(f"{category}: R$ {total:.2f}")

print("\nRevenue by month:")
for month, total in revenue_by_month.items():
    print(f"{month}: R$ {total:.2f}")

print(f"\nTop revenue month: {top_revenue_month} (R$ {revenue_by_month[top_revenue_month]:.2f})")

print("\nTop revenue product by category:")
for category, product in top_product_by_category.items():
    print(f"{category}: {product}")