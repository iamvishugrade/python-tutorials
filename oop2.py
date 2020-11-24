# class variable

# circle --> radius --> cirumference

# class Circle:
#     def __init__(self,radius,pi):
#         self.r = radius
#         self.pi = pi
#     def cal_circum(self):
#         return 2*self.pi*self.r

# c1 = Circle(5,3.14)
# c2 = Circle(4,3.14)
# print(c1.cal_circum()) # not a good way



# class Circle:
#     pi =3.14
#     def __init__(self,radius):
#         self.r = radius
#     def cal_circum(self):
#         return 2*Circle.pi*self.r
# c1 = Circle(5)
# c2 = Circle(4)
# print(c1.cal_circum())

# class Person:
#     count = 0 #class variable
#     def __init__(self,name,age):
#         Person.count+=1
#         self.name = name
#         self.age = age

# p1 = Person("vivek",24)
# p2 = Person("sumit",21)
# p3 = Person('tushar',24)
# print(Person.count)    

#####################

# 1--> encapsulation
# 2 --> abstraction
# 3 --> special naming convention
# 4 --> name mangling (__name) --> rule

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = price

    def make_a_call(self,mobile_num):
        print(f"calling {mobile_num}....")
    def full_name(self):
        return f"{self.brand} {self.model}"
    def msg(self):
        pass #--> twillo
phone1 = Phone("nokia",'1100',1200)

# phone1._price = 80000

print(phone1._price)
print(phone1.__price)
# phone1.__price=80000
print(phone1._Phone__price)