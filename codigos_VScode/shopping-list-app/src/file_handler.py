def save_to_file(shopping_list):
    with open('data/shopping_list.txt', 'w') as file:
        for product, quantity in shopping_list.items():
            file.write(f"{product}: {quantity}\n")