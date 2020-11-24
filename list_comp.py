# print squres of 1 - 10

# s = []
# for i in range(1,11):
#     s.append(i**2)
# print(s)

# squre = [i**2 for i in range(1,11)]
# print(squre)

# l = [1,2,3,4,5]
# neg = [lisa for lisa in range(1,11)]
# print(neg)

# n = []
# for i in range(1,11):
#     n.append(-i)
# print(n)

# name = ['vivek','ayushi','tushar']
# new_list = []
# for i in name:
#     new_list.append(i[0])
# print(new_list)

# lst = [i[0] for i in name]
# print(lst)

#with hust list comp

# l = ['abc','tuv','xyz']
# rev= [i[::-1] for i in l]
# print(rev)

#with funtion and list comp

# def rev_str(l):
#     return [i[::-1] for i in l]
# print(rev_str(l))



# nums = list(range(1,11))
# ev_num = []
# for lisa in nums:
#     if lisa%2==0:
#         ev_num.append(lisa)
# print(ev_num)

# ev_num = [lisa for lisa in range(1,11) if lisa % 2==0]
# print(ev_num)

# odd_num = [lisa for lisa in range(1,11) if lisa%2 != 0]
# print(odd_num)

# lst = [1,2,3,4,5,['vivek',5,6,7],True,False,None]
# def to_str(l):
#     return [str(i) for i in lst if (type(i)==int or type(i)==float)]
# print(to_str(lst))

#list comp with if else

# output-->[-1,4,-3,16]

# nums = list(range(1,11))
# new_list = []
# for lisa in nums:
#     if lisa%2==0:
#         new_list.append(lisa**2)
#     else:
#         new_list.append(-lisa)
# print(new_list)

# new_lst2 = [lisa**2 if lisa%2==0 else -lisa for lisa in range(1,11)]
# print(new_lst2)

#nested list

# output-->[[1,2,3],[1,2,3],[1,2,3]]

# nes = [[i for i in range(1,4)] for j in range(3)]
# print(nes)


