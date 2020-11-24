# dict comprihension

# sq = {1:1,2:4,3:9}
# squre = {lisa:lisa**2 for lisa in range(1,11)}
# # print(squre)

# for k,v in squre.items():
#     print(f'squre of {k} is {v}')

# for lisa,tom in sq.items():
#     print(f"squre of {lisa} is {tom}")

# name = "vivek"
# d = {lisa:(name.count(lisa)) for lisa in name}
# print(d)

#dict comp with if

# odd_even={1:'odd',2:'even'}

# odd_even = {lisa:('even' if lisa%2==0 else 'odd') for lisa in range(1,11)}
# print(odd_even)

# for i,j in odd_even.items():
#     print(f"{i} is {j}")


# odd_even = {}
# for i in range(1,11):
#     if i%2==0:
#         odd_even[i]='even'
#     else:
#         odd_even[i]='odd'
# print(odd_even)

####################

# s = {i**2 for i in range(1,11)}
# print(s)

# lst = ['vivek','ankit','mukul']
# f = {i[0] for i in lst}
# print(f)