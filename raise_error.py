### raise error

# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))
# print(num1+num2)


# def mul(a,b):
#     if ((type(a) is int) and (type(b) is int)):
#         return a*b
#     raise TypeError("oops! you enter wrong data type")

# print(mul(3,'5'))

## NotimppimentedError

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def sound(self):
#         raise NotImplementedError('you have to define this method inside the class')
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
    
#     def sound(self):
#         return "bhow bhow"

# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
    
#     def sound(self):
#         return "meo meo"

# doggy = Dog("tommy",'pug')
# catty = Cat('white','brown')

# # print(doggy.sound())
# # print(catty.sound())



############ error handling , exception handling

# try
# except
while True:

    try:
        age = int(input("please enter your age: "))
        break
    except ValueError:
        print("maybe you enterd wrong input please input in int: ")

    except:
        print("unexpected error")

if age > 18:
    print("you can play this game")
else:
    print("you can't")



#####

# try
# except
# else
# finally


# while True:
#     try:
#         num = int(input("please enter you num: "))
#     except ValueError:
#         print("please input in integer: ")
#     except:
#         print("unexpected error")
#     else:
#         print(f"number enterd by you is {num}")
#     finally:
#         print("finally block called")














# class Animal:
#     def __init__(self,name):
#         self.__name = name
    
# dog = Animal("tommy")
# # dog._name = "tuffy"
# print(dog._Animal__name)

# # print(dog.__dict__)