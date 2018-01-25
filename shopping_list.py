import json
import sys

shopping_list = {}
filename = 'shopping_list.json'

while True:

#    if filename:
#        with open(filename, 'r') as f_obj:
#            datastore = json.loads(filename.read())
#            for k, v in datastore.items():
#                print(k + ' ' + v)    
     
    list_item = input('What item would you like to add?: ').title()
    qty_item = input('How much? (enter "q" to exit at any time): ').title()
    
    if list_item == 'Q' or qty_item == 'Q':
        sys.exit()
    
    def print_list(items_dict, left_width, right_width):
        print('Shopping List'.center(left_width + right_width, '-'))
        for k, v in items_dict.items():
            print(k.ljust(left_width, '.') + str(v).rjust(right_width))
    
    shopping_list[list_item] = qty_item
    print_list(shopping_list, 20, 6)
            
    with open(filename, 'a') as f_obj:
        json.dump(shopping_list, f_obj)
        #print('List saved to "shopping_list.json"')