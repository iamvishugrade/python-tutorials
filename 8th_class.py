#default parameters

# def userr_info(f_name,l_name,age=44):
#     print(f"hello your first name is {f_name}")
#     print(f"hello your last name is {l_name}")
#     print(f"hello your age is {age}")

# userr_info('vivek','sharma')


###########################################3
# List

#list orderd collection of items
#list mutable
#list allow indexing and slicing
#list can stored any data type


# nums = [1,2,3,4,5,6]
# print(nums)
# print(type(nums))

# mix = [1,2,3,'apple','mango',2.7,7.0,None,True]
# print(mix)
# print(mix[-3])
# print(mix[1:5])
# print(mix[::-1])

#list add data 
#1--> append
#2--->insert
#3-->extend

#append

# colour = []
# print(colour) #[]
# colour.append('red')
# colour.append('white')
# print(colour)

#insert
# fruits = ['grapes','mango']
# fruits.insert(1,'kiwi')
# print(fruits)

#extend

# colour1 = ['blue','black','dark blue']
# colour2 = ['light blue','sky blue']

# colour1.extend(colour2)
# print(colour1)

# colour1.append(colour2)

# print(colour1)
# print(colour1[3])

################
#remove data froom list

#pop
#remove
#del operator

# colour = ['blue','blck','pink','red']
#pop()

# colour.pop(1)
# colour.pop()
# print(colour)

# delete operator

# del colour[0]
# print(colour)

#remove

# colour.remove('pink')
# print(colour)

## in keyword
# colour = ['blue','blck','pink','red','gray','yellow','white']
# if "red" in colour:
    # print("present")
# else:
    # print("not present")

#############
#sort()
#reverse --> key
#clear
#copy
#sorted function
#count

# colour = ['blue','blck','pink','red','gray','yellow','white']
# print(colour.count('blue'))
# nums = [90,7,8,5,66,67,34]
# colour.sort()
# print(colour)
# nums.sort()
# print(nums)

# s = sorted(nums,reverse=True) #-->it only return new list sorted manner but our old list remain same
# print(s)
# print(nums)


#clear method

# nums = [90,7,8,5,66,67,34]
# nums.clear()
# print(nums)

#copy()
# nums = [90,7,8,5,66,67,34]
# num1 = nums.copy()
# print(num1)

# num1.clear()
# print(num1)
# print(nums)
# nums = [90,7,8,5,66,67,34]
# num2 = nums
# print(num2)
# print(num2 is nums)

# num2[0]="vivek"
# num2.clear()
# print(num2)
# print(nums)


#compare 
# ==
# is

# colour = ['blue','blck','pink']
# colour1 = ['blue','blck','pink']

# print(colour==colour1) # check values
# print(colour1 is colour) # memory allocation