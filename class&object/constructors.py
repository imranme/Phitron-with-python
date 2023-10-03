class phone:
    manufactured = 'China'

    def __init__(self, brand, owner, price):
        self.brand = brand
        self.owner = owner
        self.price = price

    def send_sms(sel,phone,sms):
        text = f'sending to: {phone} {sms}'
        print(text)

my_phone = phone('sumsung', 'khan', 35435)
print(my_phone.brand, my_phone.owner, my_phone.price)

her_phone = phone('iphon', 'borolox', 2000000)
print(her_phone.brand, her_phone.owner, her_phone.price)

dad_phone = phone('nokia', 'dad', 1200)
print(dad_phone.brand, dad_phone.owner, dad_phone.price)