# user_id = ['user1','user2','user3']
# names = ['vivek','tushar','nikhil']
# print(list(zip(user_id,names)))

# d = [('a',1),('b',2),('c',3)]
# print(dict(d))

# l1 = [1,3,5,7]
# l2 = [2,4,6,8]

# * operator

# l = [(1,2),(3,4),(5,6),(7,8)]
# l1,l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))

# l1 = [1,89,80,7]
# l2 = [77,4,6,90]

# new_list = []
# for lisa in zip(l1,l2):
#     new_list.append(max(lisa))
# print(new_list)


########## any & all function

# num1 = [2,4,6,8,10]
# num2 = [1,3,5,7,9,6]

# print(all([True,True,True,False]))

#all + list comp

# print(all([lisa%2==0 for lisa in num2]))

#any 
# print(any([lisa%2==0 for lisa in num2]))


#############
#advance min(),max()

# nums = [1,2,3,4,55,66,76]
# print(max(nums))
# print(min(nums))

# names = ['vivek','tushar','xy','dxfthfghvftdtctrrvryfyyu']
# print(max(names))
# print(min(names))
# def func(item):
    # return len(item)
# print(min(names,key=func))


# students = [
    # {'name':'vivek','score':90,'age':7},
    # {'name':'tushar','score':80,'age':23},
    # {'name':'anjali','score':75,'age':24}
# ]

# print(min(students,key=lambda item: item.get('age')))

#advance sorted

# colour = ["blue",'yellow','green','red']
# colour.sort()
# print(colour)

# t = ("blue",'yellow','green','red')
# t.sort()
# print(t)

# print(sorted(t))

# mobile = [
#     {'brand':'oneplus',"price":36000,'model':'6t'},
#     {'brand':'samsung',"price":80000,'model':'s9+'},
#     {'brand':'nokia',"price":1200,'model':'1100'}
# ]

# print(sorted(mobile,key=lambda d:d['price'],reverse=True))

##more about function

#what is docsring

# def add(a,b):
    # '''this function will take 2 numbers and return sum of them'''
    # return a+b
# print(add(8,9))
# print(add.__doc__)

# print(sorted.__doc__)

