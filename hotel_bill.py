
menu = {
    "Paneer Tikka": 180,
    "Veg Manchurian": 150,
    "French Fries": 80,
    "Paneer Butter Masala": 220,
    "Dal Makhani": 180,
    "Veg Biryani": 200,
    "Pizza": 250,
    "Burger": 120,
    "Momos": 100,
    "Cold Drink": 50,
    "Coffee": 70,
    "Mango Shake": 120
}

print("=" * 50)
print("              WELCOME TO")
print("            RAJPUT PALACE HOTEL")
print("=" * 50)

print("\n🍽️  OUR MENU")
print("-" * 50)

for item, price in menu.items():
    print(f"{item:<25} ₹{price}")

order_total = 0
order = []

while True:

    item = input("\nEnter the name of item you want to order: ")

    if item in menu:
        quantity = int(input("How many quantity do you want?: "))

        total = quantity * menu[item]
        order_total += total
        order.append((item, quantity, menu[item]))

        print(f"Your item {item} has been added to your order.")

    else:
        print(f"Your item {item} is not available!")

    another_order = input("Do you want another item? (Yes/No): ")

    if another_order.lower() == "no":
        break

discount = int(input("\nEnter Discount %: "))

print("\n" + "=" * 50)
print("              YOUR BILL")
print("=" * 50)

for item, quantity, price in order:
    print(f"{item:<25} {quantity} X ₹{price} = ₹{quantity * price}")

print("-" * 50)
print(f"TOTAL AMOUNT       = ₹{order_total}")

discount_amount = (order_total * discount) / 100
final_amount = order_total - discount_amount

print(f"DISCOUNT ({discount}%)     = ₹{discount_amount:.2f}")
print(f"AFTER DISCOUNT     = ₹{final_amount:.2f}")

gst_rate = 5
gst_amount = final_amount * gst_rate / 100

print(f"GST ({gst_rate}%)          = ₹{gst_amount:.2f}")

grand_total = final_amount + gst_amount

print("-" * 50)
print(f"GRAND TOTAL        = ₹{grand_total:.2f}")

print("=" * 50)
print("       THANK YOU! VISIT AGAIN ❤️")
print("=" * 50)






