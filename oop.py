#1 abstraction 
#2 encapsulation
#3 inheritence
#4 polymorephism

# class,object<instance>,method

#list class

# l = list()
# print(l)
# l.append(7)
# print(l)

# class Person:
#     def __init__(self,first_name,last_name,age):
#         print("init method called")
#         self.f_name = first_name
#         self.l_name = last_name
#         self.age = age

# p1 = Person('vivek','sharma',43)
# p2 = Person('tushar','tyagi',24)

# print(p1.f_name)
# print(p2.age)
# print(type(p1))


# class Android:
#     def __init__(self,brand_name,model_name,price): #costructer
#         #instace variable
#         self.brand = 'sansung'
#         self.model = model_name
#         self.price = price
#         self.full_spec = brand_name+' '+model_name+' '+str(price)

# android1 = Android('samsung','s9',56000)

# print(android1.price)
# print(android1.full_spec)

#INSTANCE METHODS


# l = [1,2,4,5,6]
# l.pop()
# print(l)

# class Person:
#     def __init__(self,first_name,last_name,age):
#         # print("init method called")
#         self.f_name = first_name
#         self.l_name = last_name
#         self.age = age
#     def full_name(self):
#         return f"{self.f_name} {self.l_name}"
#     def is_above_18(self):
#         return self.age>18
# p1 = Person('vivek','sharma',43)
# p2 = Person('tushar','tyagi',24)
# print(p1.full_name())
# print(p2.is_above_18())
# print(Person.full_name(p1))




# l = [1,2,3,4,5,6,7,8,9]
# l.clear()
# print(l)
# list.clear(l)
# print(l)
# l.append(8)
# list.append(l,10)
# print(l)
