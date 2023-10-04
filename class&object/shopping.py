class shopping:
    def __init__(self, name):
        self.name =name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product ={'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
        #homework
    def remove_item(self, item):
        pass

    def chekout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if amount <total:
            print(f'please provide {total-amount}')
        else:
            extra = amount -total
            print(f'print your extra mony {extra}')

        

alin = shopping('alin swapon')
alin.add_to_cart('alue', 50, 6)
alin.add_to_cart('dim', 12, 12)
alin.add_to_cart('rice', 100, 2)

print(alin.cart)
alin.chekout(16000)
