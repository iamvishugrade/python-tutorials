# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# func(name='python',version='3.8',year=2020)

# d= dict(name="vivek",last_name="sharma")
# print(d)

# def func(**kwargs):
#     for lisa,tom in kwargs.items():
#         print(f"key is {lisa} and value is {tom}")

# func(name="vivek",l_name="sharma",age=90)


# user = {'name':'vivek','mobile':"oppo",'laptop':'dell'}
# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}-->{v}")
# func(**user)


########## PADK ##########
# p --> prameter
# A --> *args
# D --> default parameter
# K --> kwrgs

# def func(name,*args,last_name="sharma",**kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)
# func(1,2,3,4,5,6,7,8,last_name="agarwal",a=55,b=6)

################# summry ###############

# def mul(a,b):
#     return a*b
# print(mul(4,5))

# def total(*args):
#     t = 0
#     for i in args:
#         t+=i
#     return t
# print(total(1,2,3,4,5))

# def func(**vivek):
#     print(vivek)
#     print(type(vivek))
# func(name="ankit",age=24)