def call(): #methods 
    print('calling someone i dont khow')
    return 'call done'
class phone:
    price = 13000
    color = 'blue'
    brand = 'samsung'
    features = ['cemera', 'speakar', 'hemer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone,sms):
        text= f'sending SMS to: {phone} and message: {sms}'
        return text 


my_phone = phone()
print(my_phone.price)
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(234332, 'ami bari jabo na')
print(result)
