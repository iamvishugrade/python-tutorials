# lambda parameter_list: expression
# --> anonymous function
# def add(a,b):
#     return a+b
# print(add(4,5))

# add = lambda a,b:a+b
# print(add(2,3))

# mul = lambda a,b:a*b
# print(mul(5,6))

# print(add)

# def is_even(n):
#     return n%2==0
# print(is_even(8))

# even = lambda n:n%2==0
# print(even(0))

# def last(s):
#     return s[-1]
# print(last("vivek"))

# l = lambda s:s[-1]
# print(l("sharma"))

# def func(s):
#     if len(s)>=5:
#         return True
#     return False

# print(func("vivek"))


# f = lambda s:True if len(s)>=5 else False
# print(f("sharma"))

# special inbuilt function 

# 1--> enumerate
# 2-->map
# 3-->filter


############## enumurate ###########
# name = ["vivek","tushar","nikhil"]
# pos = 0
# for lisa in name:
#     print(f"{pos} --> {lisa}")
#     pos+=1

# for pos,lisa in enumerate(name):
#     print(f"{pos} --> {lisa}")

# user = ["vivek","harsh","anshu","ayushi"]
# def find_pos(l,target):
#     for pos,lisa in enumerate(l):
#         if lisa == target:
#             return pos
#     return "not found"

# print(find_pos(user,'anshu'))

## map function
# map function value-->ittreable 

# nums = [1,2,3,4,5,6,7,8,9]
# new = []
# for i in nums:
#     new.append(i**2)
# print(new)

# new = [i**2 for i in range(1,10)]
# print(new)

# nums = list(range(1,10))
# def square(a):
#     return a**2
# print(list(map(square,nums)))

# print(list(map(lambda a:a**2,nums)))


# lst = ['abcd','abc','defgsgg']
# lenght=map(len,lst)
# # print(lenght)
# # for i in lenght:
# #     print(i)
# # for j in lenght:
# #     print(j)
# new = list(lenght)

# nums = [1,2,3,4,5,6,7,8,9,10]
# def even(n):
#     return n%2==0
# var = tuple(filter(even,nums))
# print(var)



# print(list(filter(lambda a:a%2==0,list(range(1,11)))))

# dict,list,tuple,set,str

#### itreble & ittreator


# nums = [1,2,3,4,5]   #--> itrable
# sq = map(lambda a:a**2,nums) #--> itretor
# print(sq)

# for i in sq:
#     print(i)

# for lisa in nums:
#     print(lisa)

# for j in sq:
#     print(j)
# for tom in nums:
#     print(tom)

# behind the scene of itrble

# 1--> iter function
# 2--> iter(lisa)-->ittreator
# 3--> next(iter(lisa))

# nums = [1,2,3,4,5]
# num_iter = iter(nums)
# print(next(num_iter))
# print(next(num_iter))S
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))

# sq = map(lambda a:a**2,nums)
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))