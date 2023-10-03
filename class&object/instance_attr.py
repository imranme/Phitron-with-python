class shop:
    shopping_mall = 'Bosundhora'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # instance attributes
    
    def add_to_cart(self, item):
        self.cart.append(item)

sagor = shop('sagor_bhai')
sagor.add_to_cart('sari')
sagor.add_to_cart('gohona')
print(sagor.cart)

mamun = shop('mamun_bro')
mamun.add_to_cart('benarosi')
mamun.add_to_cart('gold')
print(mamun.cart)

    