# main.py

from shopping_list import ShoppingList
from file_handler import save_to_file

def display_menu():
    print("Menu:")
    print("1. Add product")
    print("2. View shopping list")
    print("3. Finalize list and save")
    print("4. Exit")

def main():
    shopping_list = ShoppingList()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            product = input("Enter product name: ")
            quantity = input("Enter quantity: ")
            shopping_list.add_product(product, quantity)
        elif choice == '2':
            shopping_list.display_list()
        elif choice == '3':
            save_to_file(shopping_list.get_list())
            print("Shopping list saved.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()