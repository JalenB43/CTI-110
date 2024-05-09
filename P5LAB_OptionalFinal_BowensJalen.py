#Jalen Bowens
#5/9
#P5LAB Advanced Possible Final 
#Use of loops, functions and module import to complete assignments


# create a dictionary
def create_dict():
    grocery_items = {
        "apples" : 3.69,
        "berries" : 4.00,
        "chocolate" : 2.89,
        "turkey" : 6.99,
        "cheese" : 4.00,
        "pepsi" : 7.89,
        "eggs" : 3.50,
        "bread" : 3.00
        }
    return grocery_items
# create a function to display dictioanry
def show_avail_items(grocery):
    print("Grocery Item",'\t','\t',"Price")
    print("-"*30)
    for key, value in grocery.items():
        #print(key,'\t','\t','\t', value)
        print(f'{key:<25}{"$"}{value:<12.2f}')
    print("-"*30)
    
def add_to_cart(grocery):
    for key in grocery.items():
        cart_list[]
        list(grocery_items.key())
    
    

    
    print("*Welcome to the Grocery Checkout*")
    print()
    item=input("Enter an item to add"+ " to the cart or 'Done' to stop adding items: ")
    if item !='Done':
        cart_list.append(item)
    #item=input("Enter an item to add"+ " to the cart or 'Done' to stop adding items: ")
     #elif item =='Done':
    # continue


#def show_cart(add to cart):
    #print("The items currently in your list are: ")
#def calc_total
        
        



def main():
    grocery = create_dict()
    show_avail_items(grocery)
    add_to_cart(grocery)



main()
