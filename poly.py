#special magic method / dunder method, operator overloading, polymorephism
class Phone:
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
    def full_name(self):
        return f"{self.brand} {self.model}"
    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"Phone(\'{self.brand}\',\'{self.model}\',\'{self.price}\')"
    
    def __len__(self):
        return len(self.brand)

    def __add__(self,self2):
        return self.brand+self2.brand


phone1 = Phone('nokia','1100',1000)
phone2 = Phone("samsung",'gt1890',3000)
# print(phone1)

print(phone1+phone2)
# print(len(phone2))

# print(str(phone2))
# print(repr(phone2))

#str,repr

# l = [1,2,3]
# print(len(l))
# t = (1,2,3,4,5,)
# print(len(t))
# # print(l)

# 2+3 = 5
# "vivek"+"sharma"  = viveksharma