# Kao Yang
# CSD-325
# Module 2 - Documented Debugging + Flowchart


def calculate_total(price, quantity):
    total = price * quantity
    return total


def main():
    print("Item Total Calculator")

    price = float(input("Enter the price of the item: $"))
    quantity = int(input("Enter the quantity: "))

    total = calculate_total(price, quantity)

    print(f"Your total is: ${total:.2f}")


if __name__ == "__main__":
    main()
