# user_info = {
#     "name":'vivek sharma',
#     'age':24,
#     'fav_movies':['tangled','chhichore','3 idiot'],
#     'fav_colour':['blue','white','red']
# }
# print(user_info)

# user_items = user_info.items()
# print(type(user_items))

# for i,j in user_info.items():
    # print(f"key is {i} and value is {j}")


# how to add data

#as we know this
# user_info = {
#     "name":'vivek sharma',
#     'age':24,
#     'fav_movies':['tangled','chhichore','3 idiot'],
#     'fav_colour':['blue','white','red']
# }

# user_info['fav_songs']=['song1','song2','song3']
# print(user_info)


### pop and popitem

# poped_item = user_info.pop('fav_songs')

# print(poped_item)
# print(user_info)

# p_item = user_info.popitem()
# print(p_item)
# print(user_info)
# user_info.popitem()
# print(user_info)

#update method

# user_info = {
#     "name":'vivek sharma',
#     'age':24,
#     'fav_movies':['tangled','chhichore','3 idiot'],
#     'fav_colour':['blue','white','red']
# }

# more_info = {
#     'state':'delhi',
#     'company_name':'2pointeducation'
# }

# user_info.update(more_info)

# print(user_info)

#fromkeys method ---> we use this when we want to set default values

# d = {'name':'unknown','age':'unknown'}
# print(d)

# d1 = dict.fromkeys(['nama','age','hight','income'],'unknown')
# print(d1)

# d2 = dict.fromkeys(('nama','age','hight','income'),'unknown')
# print(d2)

# d3 = dict.fromkeys(('a','b','c'),'none')
# print(d3)

# d4 = dict.fromkeys('abcdefghij','we are gud')
# print(d4)

#get method

# user_info = {
#     "name":'vivek sharma',
#     'age':24,
#     'fav_movies':['tangled','chhichore','3 idiot'],
#     'fav_colour':['blue','white','red']
# }

# print(user_info['names']) #--> error

# print(user_info.get('names'))

# print(user_info.get('collge','key is not present'))
# if user_info.get('names'): #--> false
#     print("present")
# else:
#     print('not present')

#clear method

# user_info.clear()
# print(user_info)

#copy method

# d = {'name':'vivek','age':24}
# # print(d)
# d1 = d.copy()
# print(d1)

# print(d1==d)
# print(d1 is d)

# overriding key value

# user = {'name':'vivek','age':33,'name':'nikhil','age':0}
# print(user['name'])
# print(user['age'])

######################################
# some programms
# progrmm of squre finder

# {key:key**2}

# def squre_finder(n):
#     s = {}
#     for i in range(1,n+1):
#         s[i]=i**2
#     return s
 
# print(squre_finder(10))


# letter counter in a word

# def letter_count(s):
#     count = {}
#     for lisa in s:
#         count[lisa]=s.count(lisa)
#     return count
# print(letter_count('vivek'))

# user = {}
# name=input("enter your name: ")
# age= int(input("enter your age: "))
# fav_colour = input("plese enter your fav colours comma sapreted: ").split(",")

# user['n']=name
# user['ag']=age
# user['f_c']=fav_colour

# for key,values in user.items():
#     print(f" key {key}:values is {values}")


################# summary #########

# d = {'name':'vivek','age':24}
# print(d)

# d1 = dict(name='vivek',age=44)
# print(d1)

# print(d['name'])
# print(d.get('ages','i don\'t know'))

# for i in d1:
#     print(i)

# for i in d.values():
#     print(i)

# for i,j in d.items():
    # print(i,j)

# if 'name' in d:
#     print("yes")
# else:
#     print('no')