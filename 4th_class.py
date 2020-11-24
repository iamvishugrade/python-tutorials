# precedence rules
# + - * / % = == != < > <= >= 
# ** --> power 


# print(2-2+1)  # + - same precedence left to right

# print(2*2//2 % 2) # * / // % same precendece
    #    4//2%2
    #    2%2
    #    0--> output
   

# print(3**3)

# print(2**3**2) #2**9

# print((2+2-1)/2**3)  # power braces (multiply devide mod) (plus minis )
    #   2+2-1/8
    
# print(3/2**3)
# print(3/8)
 
# braces
# power
# mul,devide,modulas (left to right)
# plus,minus (left to right)


# string formating

# name = "vivek"
# print(name.count('k'))

# name = "vivek sharma"
# age = 54

# print("hello"+" "+name+" "+"your age is"+' '+str(age))  #umcoomon way   

# format 
# f string --> fast string

# print(f"hello {name} your age is {age}")


#if elif else

# age = int(input("enter your age: "))

# if age>18:
#     print("you can play this game...")
# else:
#     print("sorry you are underage!")


# num = int(input("enter your number: "))

# if num%2==0:
#     # 4%2
#     # 0==0--> True
#     print("number is even")
#     print("you are good..")
# else:
#     print("no. is odd")

#nested if else

######## number guessing game

# winnig_num = 39
# user_input = int(input("guess a number b/w 1 to 100: "))

# if user_input==winnig_num:
#     print("cogrts!!! you won")
# else:
#     if user_input<winnig_num:
#         print("too low")
#     else:
#         print("too high")


# and or not

# a = "abc"
# b = 10

# if a=='abc' and b==11:
#     print("true")
# else:
#     print("false")

 ###or
# a = "abc"
# b = 10

# if a=='abc' or b==11:
#     print("true")
# else:
#     print("false")

# prctc-->gretest of three number 


