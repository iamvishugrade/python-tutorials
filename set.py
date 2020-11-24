# []--> list
# ()--> tuple
# {1,2,4,'vhgu'}--> set

########## set #########

# 1--> unorded collection of data

# s = {1,2,2,4,6,7,3,4,5,6,7}
# print(s)

# Why we use set?
# to remove duplicates

# lst = [1,2,3,4,5,6,5,5,4,3,33,6,33]
# s = set(lst)
# print(list(s))

#methods in set

# s = {1,2,3}
# s.add(4)
# print(s)
# s.add(88)
# print(s)

# s.remove(1)
# print(s)
# s.discard(3)
# print(s)

# s.remove(1) #--> error
# print(s)

# s.discard(1)
# print(s)

# s.clear()
# print(s)

# s = {1,2,3}
# s1 = s.copy()
# print(s1)

# s = {1,2,3,4,5,'vivek'}
# print(s)

# s1 = {1,2,[1,3,4]} #--> error
# print(s1)

# s={1,2,3,4,5}
# if 5 in s:
    # print("present")
# else:
    # print("not present")

# s={1,2,3,4,5,'vivek','sharma',66}

# for lisa in s:
    # print(lisa,end=" ")

# 
# union | (pipe)
# intersection & (and)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# union_set = s1|s2
# print(union_set)

# s1 = {1,2,3,4,5,6,7}
# s2 = {5,4}

# intersct = s1&s2
# print(intersct)