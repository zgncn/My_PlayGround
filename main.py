#Create the item_list
item_list=["Laptop","Headset","Second monitor","Mousepad","USB drive","External drive"]
#Assign the spending limit value to a variable called limit
limit=5000
#Create a dictionary that contains each item and its price
price_sheet={"Laptop":1500,
             "Headset":100,
             "Second monitor":200,
             "Mousepad":50,
             "USB drive":70,
             "External drive":250

}
#Initialize the cart list
cart=[]
#Define the "add_to_cart" function
def add_to_cart(item,quantity):  #quantity=miktar
    cart.append((item,quantity))
    item_list.remove(item)
#Define the "create_invoice" function
#📌 The "create_invoice" function should calculate the taxes of each item (18%) and add it to the total amount.
def create_invoice():
    total_amount_inc_tax=0
    for item,quantity in cart:
        price=price_sheet[item]
        tax=0.18 *price
        total = (tax +price) *quantity
        total_amount_inc_tax += total
        print("Item",item,"\t", "Price",price,"\t","Quantity",quantity,"\t","Tax",tax,"\t","Total",total,"\n")
    print("After the taxes are applied the total amount is",total_amount_inc_tax)
    return total_amount_inc_tax

#Define a function for the checkout.
#📌 The "checkout" function should subtract the total amount
#from the budget and print a statement to inform if the payment was successful.
def checkout():
    global limit
    total_amount=create_invoice()
    if limit==0:
        print("You dont have any budget.")
    elif total_amount>limit:
        print("You have to drop some items.")
    else:
        limit -=total_amount
        print(f"The total amount(incl. taxes) you've paid is: {total_amount}.You have {limit} dollars left ")

add_to_cart("Laptop",1)
add_to_cart("Headset",8)
add_to_cart("Second monitor",1)
add_to_cart("Mousepad",1)
add_to_cart("USB drive",2)
add_to_cart("External drive",4)

#call the checkout function to pay for all your items
checkout()


