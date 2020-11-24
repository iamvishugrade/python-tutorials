# def add(num1,num2):
#     return num1+num2
# print(add(5,5))

###
# astrisk

# *args

# def all_total(*args):
#     total=0
#     print(type(args))
#     for lisa in args:
#         total+=lisa
#     return total
# print(all_total(1,2,3,4,5))


# def all_mul(*args):
#     mul = 1
#     for i in args:
#         mul*=i
#     return mul
# print(all_mul(1,2,3,4,5,6))

## args with normal parameter

# def add_all(num1,*args):
#     total = 0
#     print(num1)
#     # print(num2)
#     print(args)
#     print(type(args))
#     for i in args:
#         total+=i
#     return total
# print(add_all(1,2,3,4,5,6,7,8,9,10))


# nums =(1,2,3,4,5,6,7,8,9,10)
# def add_all(*args):
#     print(type(args))
#     total = 0
#     for i in args:
#         total+=i
#     return total
# print(add_all(*nums))

# def concate_str(*args):
#     full_name = ''
#     for i in args:
#         full_name+=i
#     return full_name
# print(concate_str('vivek','@','sharma'))

#prctc
#  2   2,3,4,5
# (num,*args)
# i**num