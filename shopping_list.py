import json
import sys

filename = 'shopping_list.json'
shopping_list = {}

def print_list(items_dict, left_width, right_width):
    print('Shopping List'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))

def add_items():
    while True:
        list_item = input('What item would you like to add?: ').title()
        if list_item == 'Q':
            sys.exit()
        qty_item = input('How much? (enter "q" to exit at any time): ').title()
        if qty_item == 'Q':
            sys.exit()
        shopping_list[list_item] = qty_item
        print_list(shopping_list, 20, 6)
        with open(filename, 'w') as f:
            json.dump(shopping_list, f)

try:
    with open(filename, 'r') as f:
        shopping_list = json.load(f)
        print_list(shopping_list, 20, 6)
        alter_list = input('Would you like to add anything else?: ').title()
        if alter_list == 'Y':
            add_items()
        elif alter_list == 'N':
            sys.exit()
except FileNotFoundError:
    print("No existing shopping list...")
    add_items()



