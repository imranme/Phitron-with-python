class pen:
    menufactured = 'Bangladesh'

    def __init__(self, owner, brand, price, color):
        self.owner = owner
        self.brand = brand
        self.price = price
        self.color = color

my_pen = pen('me', 'toper', 10, 'red')
print(my_pen.owner, my_pen.brand, my_pen.price, my_pen.color)

frend_pen = pen('dst', 'Goodluk', 12, 'blak')
print(frend_pen.owner, frend_pen.brand, frend_pen.price,frend_pen.color)

sir_pen = pen('sir', 'High Scholl', 15, 'red')
print(sir_pen.owner, sir_pen.brand, sir_pen.price,sir_pen.color)


class football:
    maker = 'Bangladesh'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

frender_football = football('frend', 'nike', 2500)
print(frender_football.owner, frender_football.brand, frender_football.price)

amaer_football = football('ami', 'diar', 500)
print(amaer_football.owner, amaer_football.brand, amaer_football.price)



class batt:
    menufactured = 'Bangladesh'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

may_batt= batt('anamul', 'kokobora', 25000)
print(may_batt.owner, may_batt.brand, may_batt.price)

he_batt = batt('musfik', 'Ton', 50000)
print(he_batt.owner, he_batt.brand, he_batt.price)
    