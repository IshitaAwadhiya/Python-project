class ManagementApp:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Item added successfully!")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print("Item removed successfully!")
        else:
            print("Item not found!")

    def update_item(self, old_item, new_item):
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items[index] = new_item
            print("Item updated successfully!")
        else:
            print("Item not found!")

    def list_items(self):
        print("Items:")
        for item in self.items:
            print("-", item)

if __name__ == "__main__":
    app = ManagementApp()

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. List Items")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to add: ")
            app.add_item(item)
        elif choice == "2":
            item = input("Enter item to remove: ")
            app.remove_item(item)
        elif choice == "3":
            old_item = input("Enter item to update: ")
            new_item = input("Enter new item value: ")
            app.update_item(old_item, new_item)
        elif choice == "4":
            app.list_items()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
