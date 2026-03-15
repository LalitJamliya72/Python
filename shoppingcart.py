def shopping_cart(cart):
    totalcost = 0
    for item in cart:
         totalcost+=item['price']*item['quantity']
        
    return totalcost
    
cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3}
]
totalcost = shopping_cart(cart)
print(totalcost)

        