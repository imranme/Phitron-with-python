class shop:
    cart = [] #class attributes
    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)

Tushar = shop('imrans')
Tushar.add_to_cart('shoes')
Tushar.add_to_cart('phone')
print(Tushar.cart)

maruf = shop('marufa')
maruf.add_to_cart('watch')
maruf.add_to_cart('jus')
print(maruf.cart)