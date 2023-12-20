class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None  # Generated automatically by the application
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_order(self, food_items):
        self.orders.append(food_items)

    def view_order_history(self):
        if self.orders:
            print("Order History:")
            for order in self.orders:
                print(order)
        else:
            print("No order history.")

    def update_profile(self, full_name=None, phone_number=None, email=None, address=None, password=None):
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address
        if password:
            self.password = password
            
class Admin:
    def __init__(self):
        self.food_items = []  # List to store food items

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1  # Auto-generate FoodID
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = food_id
        self.food_items.append(food_item)
        print(f"Added food item: {name} with FoodID: {food_id}")

    def edit_food_item(self, food_id, new_details):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                for key, value in new_details.items():
                    setattr(food_item, key, value)
                print(f"Food item with FoodID {food_id} updated.")
                return
        print("Food item not found.")

    def view_all_food_items(self):
        if not self.food_items:
            print("No food items available.")
        else:
            print("List of all food items:")
            for food_item in self.food_items:
                print(f"FoodID: {food_item.food_id}, Name: {food_item.name}, "
                      f"Quantity: {food_item.quantity}, Price: {food_item.price}, "
                      f"Stock: {food_item.stock}")

    def remove_food_item(self, food_id):
        for idx, food_item in enumerate(self.food_items):
            if food_item.food_id == food_id:
                del self.food_items[idx]
                print(f"Food item with FoodID {food_id} removed.")
                return
        print("Food item not found.")


# Example Test Case 1:
# Create food items
food1 = FoodItem("Tandoori Chicken", "4 pieces", 240, 0, 20)
food2 = FoodItem("Vegan Burger", "1 piece", 320, 10, 15)
food3 = FoodItem("Truffle Cake", "500gm", 900, 5, 10)

# Create user
user1 = User("John Doe", "1234567890", "john@example.com", "123 Main St", "password")

# Place order
user1.place_order([food2, food3])
user1.view_order_history()

# Test update_profile method
user.update_profile(full_name="Jane Doe", address="456 Oak St")
print(f"Updated Profile - Name: {user.full_name}, Address: {user.address}")

# Create Admin instance and test food item methods
admin = Admin()
admin.add_food_item("Salad", 5, 4.99, 0.2, 10)
admin.add_food_item("Soup", 4, 3.99, 0.1, 8)
admin.view_all_food_items()  # View all food items

# Test edit_food_item method
new_item = {
    "Name": "Salmon",
    "Quantity": 3,
    "Price": 12.99,
    "Discount": 0.05,
    "Stock": 5
}
admin.edit_food_item(1, new_item)  # Edit food item
admin.view_all_food_items()  # View all food items after edit

# Test remove_food_item method
admin.remove_food_item(2)  # Remove food item
admin.view_all_food_items()  # View all food items after removal
