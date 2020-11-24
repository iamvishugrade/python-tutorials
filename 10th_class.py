###### tuples
# tuples are data structure
# tuple can store anything
# tuple orderd collection of data
# important-->tuple immuatble 
#csv in a small braes or prantheses
# colour = ('red','yellow','pink')
# print(colour)
# print(type(colour))

#not allowed
# no insert,no appeend , no remove , no pop

#allowed
# indexing,slicing,count,len func

# nums = (1,2,3,4,5,6,7)
# print(len(nums))
# print(nums[1:5])

# nums[0]=11 #--> error
# print(nums)

# mix = (1,2,3,4,5,6,7,4.0,'vivek')
# for lisa in mix:
    # print(lisa)
    # print(type(lisa))

# tuple with one element

# num1 = (1)
# print(type(num1))

# fruits = 'apple','mango','kiwi'
# print(type(fruits))
# print(fruits)

#tuple unpacking

# actor = ('jhonny deep','irfan khan','prabhas')
# hollyw,bollyw,tollyw = actor
# print(hollyw)
# print(tollyw)
# print(bollyw)

# hollyw,bollyw = actor #--> error


# random = (5,6,7,8,[1,2,3,4,5])
# random[4][0]="vivek"
# print(random)

# random[4].append("sharma")
# print(random)


# max, min, sum

# nums = (1,2,3,4,5)
# print(max(nums))
# print(min(nums))
# print(sum(nums))

#### function returning two values

# num1,num2 = input("enter two numbers comma sepreted: ").split(",")

# def add_mul(n1,n2):
#     add = n1+n2
#     mul = n1*n2
#     return add,mul
# print(add_mul(int(num1),int(num2)))
# print(type(add_mul(int(num1),int(num2))))


# num1,num2 = input("enter two numbers comma sepreted: ").split(",")

# def add_mul(n1,n2):
#     add = n1+n2
#     mul = n1*n2
#     return add,mul

# a,m=add_mul(5,4)

# print(f"addition of two number is {a}")
# print(f"mul of two number is {m}")


########### smry of tulpe ########

# nums = tuple(range(1,11))
# print(nums)
# print(list(nums))

# n = str(nums)
# print(n)
# print(type(n))
