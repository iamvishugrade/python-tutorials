# class Phone:
#     def __init__(self,brand_name,model_name,price):
#         self.brand = brand_name
#         self.model = model_name
#         # if price>0:
#         #     self.price = price
#         # else:
#         #     self.price = 0
#         self._price = max(price,0)
#         self.full_spec = f"{self.brand} {self.model} price is {self._price}"
    # def make_a_call(self,number):
    #     return f"calling {number}..."
    
    # def full_name(self):
    #     return f'{self.brand} {self.model}'

# phone1 = Phone('nokia','3310',-1100)
# phone1._price = 500
# print(phone1.brand)
# print(phone1._price)

# class Phone:
#     discount = 50
#     def __init__(self,brand_name,model_name,price):
#         self.brand = brand_name
#         self.model = model_name
#         self.price = price

#     def apply_dis(self):
#         off_price = (self.discount/100*self.price)
#         return self.price - off_price
#     mobile = Phone('samsung','s10',88000)
# mobile1 = Phone('nokia','lumia 520',8000)
# mobile1.discount = 10
# print(mobile1.__dict__)
# print(mobile.__dict__)
# print(mobile.apply_dis())
# print(mobile1.apply_dis())



######################
# INHERITANCE

# class Phone: # base class / parent class
#     def __init__(self,brand_name,model_name,price):
#         self.brand = brand_name
#         self.model = model_name
#         self.price = price

#     def make_a_call(self,number):
#         return f"calling {number}..."
    
#     def full_name(self):
#         return f'{self.brand} {self.model}'

# class Smartphone(Phone): #derived class / child class
#     def __init__(self,brand_name,model_name,price,ram,i_memory,rear_cam):
#         # Phone.__init__(self, brand_name, model_name, price) #uncommon way
#         super().__init__(brand_name, model_name, price)
#         self.ram = ram
#         self.i_memory = i_memory
#         self.rear_cam = rear_cam

# phone = Phone('nokia',1100,1000)
# android = Smartphone('onepus','5t',30000,'6GB','128 GB','20 MP')
# print(phone.full_name())
# print(android.full_name())
# print(android.make_a_call(7417234212))
# print(Smartphone.full_name(android))

#multilevel inheritnce, mro, method overriding
#mro --> method resolution order

class Phone: # base class / parent class
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price

    def make_a_call(self,number):
        return f"calling {number}..."
    
    def full_name(self):
        return f'{self.brand} {self.model}'

class Smartphone(Phone): #derived class / child class
    def __init__(self,brand_name,model_name,price,ram,i_memory,rear_cam):
        super().__init__(brand_name, model_name, price)
        self.ram = ram
        self.i_memory = i_memory
        self.rear_cam = rear_cam

class Flagship(Smartphone):
    def __init__(self,brand_name,model_name,price,ram,i_memory,rear_cam,front_cam):
        super().__init__(brand_name, model_name, price, ram, i_memory, rear_cam)
        self.front_cam = front_cam
    def full_name(self):
        return f"{self.brand} {self.model} {self.front_cam}"

phone = Phone('nokia',1100,1000)
android = Smartphone('onepus','5t',30000,'6GB','128 GB','20 MP')
flag = Flagship('samsung','s10',80000,'8gb','256gb','48mp','20mp')

# print(phone.full_name())
# print(android.full_name())
print(flag.full_name())

# print(help(Smartphone))
# print(help(Flagship))
# print(help.__doc__)

