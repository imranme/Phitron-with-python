     #  UnCommon Inhetitance 


class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'learning python and practing'
    
class Phone:
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
    
    def run(self):
        return f'hey phone go'
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
class Camera:
    def __init__(self, brand, price, color, pixel) -> None:
        self.brand =brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass
     

    #  Common Inhetitance 
    #bace class, parent class, common attribiute + function class
    #derived class, childe class, uncommon attribute + functionlity class

class Gaget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin 

    def run(self):
        return f'Running laptop: {self.brand}'
        


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'learning python and practing'
    
class Phone:
    def __init__(self, dual_sim) -> None:
        self.dual_sim = dual_sim
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass
       