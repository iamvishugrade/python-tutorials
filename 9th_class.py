#split method string to list

# user = "vivek sharma 43".split()
# print(type(user))

#join
# user =  ['vivek','sharma']
# print(",".join(user))

#looping in list

# colour = ['blue','blck','pink','purple']

# for lisa in colour:
#     print(lisa,end=" ")

# lisa = 0
# while lisa<len(colour):
    # print(colour[lisa])
    # lisa+=1

# nums = [1,2,3,4,5,6]
# for lisa in nums:
    # print(lisa**2,end=" ")

# list inside list

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(len(matrix))
# print(matrix[2])
# for lisa in matrix:
    # print(lisa)

# print(matrix[2][0:2])
# for lisa in matrix:
    # for tom in lisa:
        # print(tom,end=" ")


#################### list()

# nums = [1,2,3,4,5]
# print(nums)


# nums = list(range(1,11))
# print(nums)
# nums.pop()
# print(nums)

# nums.append('ten')
# print(nums)
# print(nums.index(10))

# poped_item = nums.pop()
# print(poped_item)

#passing list to a function

# input--> [1,2,3,4]
# output-->[-1,-2...]

# nums = list(range(1,11))
# def negative_list(l):
#     negative = []
#     for lisa in l:
#         negative.append(-lisa)
#     return negative
# print(negative_list(nums))


# nums = list(range(1,6))
# def cube(l):
#     c = []
#     for lisa in l:
#         c.append(lisa**3)
#     return c
# print(cube(nums))


#reverse method

# l = list(range(1,6))
# print(l)
# l.reverse()
# print(l)

# nums = list(range(1,6))
# def rev(l):
    # return l[::-1]

# print(rev(nums))

# nums = list(range(1,11))
# nums = [1,2,3,4,5,6,7,8,9,10]

# def rev(l):
#     r_list = []
#     for i in range(len(nums)):
#         poped_item = l.pop()
#         r_list.append(poped_item)

#     return r_list
# print(rev(nums))

# prctc set
# nums = [1,2,3,4,5,6,7,8,9,10]
# output= [[1,3,5,7,9],[2,4,6]]
#########2
# l = ['abc','tuv','xyz']
# output--> ['cba','vut','zyx']