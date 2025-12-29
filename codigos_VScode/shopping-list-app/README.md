# Shopping List Application

This is a simple command-line application that allows users to create a shopping list by entering product names and their respective quantities. Once the user has finished entering items, the application saves the shopping list to a text file.

## Features

- User-friendly menu interface for adding products and quantities.
- Ability to view the current shopping list.
- Option to finalize and save the shopping list to a file.

## Project Structure

```
shopping-list-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── shopping_list.py # Contains the ShoppingList class
│   └── file_handler.py  # Handles file operations
├── data
│   └── shopping_list.txt # File where the shopping list is saved
├── requirements.txt      # Lists project dependencies
└── README.md             # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd shopping-list-app
   ```

2. Install the required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to add products and quantities to your shopping list. Once you are done, the list will be saved to `data/shopping_list.txt`.