# Cafe Management System (Restaurant Counter Version)

class Cafe:
    def __init__(self):
        # Menu with items and prices
        self.menu = {
            "Coffee": 50,
            "Tea": 30,
            "Sandwich": 80,
            "Burger": 120,
            "Cake": 60,
            "Juice": 40,
            "Pizza":150,
            "Coffee":20,
            "Cold Coffee":100,
            "Momos":50,
            "French Fries":80,
            "Rolls":30
        }
        self.sales = []  # To store all customer transactions

    def display_menu(self):
        print("\n------ Cafe Menu ------")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")
        print("------------------------")

    def take_order(self, customer_name):
        order = {}
        print(f"\nWelcome {customer_name}! Enter your order (type 'done' when finished):")

        while True:
            item = input("Item name: ").title()
            if item.lower() == "done":
                break
            if item in self.menu:
                qty = int(input(f"Quantity of {item}: "))
                order[item] = order.get(item, 0) + qty
            else:
                print("❌ Item not in menu, please try again.")

        if order:
            self.generate_bill(order, customer_name)
        else:
            print("⚠️ No items ordered!")

    def generate_bill(self, order, customer_name):
        print("\n------ Bill ------")
        total = 0
        for item, qty in order.items():
            price = self.menu[item] * qty
            print(f"{item} x {qty} = ₹{price}")
            total += price
        print("------------------")
        print(f"Customer: {customer_name}")
        print(f"Total Amount: ₹{total}")
        print("------------------")

        # Save the sale
        self.sales.append({"customer": customer_name, "order": order, "total": total})

    def show_sales_summary(self):
        print("\n📊 Cafe Sales Summary:")
        if not self.sales:
            print("No sales yet.")
            return
        total_sales = 0
        for i, sale in enumerate(self.sales, 1):
            print(f"Order {i} | Customer: {sale['customer']} | {sale['order']} -> ₹{sale['total']}")
            total_sales += sale["total"]
        print(f"\n💰 Total Earnings Today: ₹{total_sales}")


# Main Program (Restaurant Counter)
def main():
    cafe = Cafe()

    while True:
        print("\n==== Cafe Counter ====")
        print("1. Show Menu")
        print("2. New Customer Order")
        print("3. Sales Summary")
        print("4. Close Cafe")
        
        choice = input("Enter choice: ")

        if choice == "1":
            cafe.display_menu()
        elif choice == "2":
            name = input("Enter customer name: ").title()
            cafe.take_order(name)
        elif choice == "3":
            cafe.show_sales_summary()
        elif choice == "4":
            print("✅ Cafe is now closed. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()