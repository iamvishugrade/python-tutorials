# nums = list(range(1,11))
# print(nums)
# print(max(nums)) #--> 10
# print(min(nums)) # -->1

# programme of diff of max number and min number of a list
# def mx_mn(l):
    # return max(l)-min(l)

# print(mx_mn(nums)) 

# to count sublist in a list
# lst = [1,2,3,'vivek',[8,9,0],[7,4,5]]
# def check_sublist(l):
#     counter = 0
#     for lisa in l:
#         if type(lisa)==list:
#             counter+=1
#     return counter
# print(check_sublist(lst))

#############>>>>>>> summary <<<<<<<<################

# nums = [1,2,3]
# list mutable
# list is orderd data collection
# anything can be stored in list
# indexing and slicing is alllowed

# data add--> append,extend,insert
# remove data --> pop, del[], remove method

# num1 = [1,2,3,4,5]
# num2 = ["vivek"]
# alls = num1+num2
# print(alls)

## even odd founder
# nums = list(range(1,11))
# def odd_even(l):
#     odd = []
#     even= []
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     total = [odd,even]
#     return total
# print(odd_even(nums))

#reverse of elements
# words = ['abc','tuv','xyz']
# n = []
# for i in words:
    # n.append(i[::-1]) 

# print(n)

######
# words = ['abc','tuv','xyz']
# n = []
# for i in range(len(words)):
#     n.append(words.pop()[::-1])
# print(n)