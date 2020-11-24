# open  function
#read method
#seek method
#tell method
#readline method
#readlines method
#close method

# fl = open('text1.txt')
# print(fl.read())
# print(fl.read())
# print(fl.tell())  # --> cursor postion
# fl.seek(0)
# print(fl.tell())
# print(fl.read())
# print(fl.readline(),end="")
# print(fl.readline())

# lines = fl.readlines()
# print(len(lines))


##

# 1-> Name
# 2--> closed
# print(fl.name)
# 
# print(fl.closed)
# fl.close()
# print(fl.closed)


# new = open("F:\\python practice\\new.txt")
# print(new.read())
#windows \
#linux/
#mac/

# with block

# with open(r"F:\python practice\new.txt") as fl:
    # print(fl.read())

# print(fl.closed)



##############  file writing

# w,a,r+
# with open("text2.txt",'w') as fl:  # data override
    # fl.write("this is for text 2 file")

# with open("text3.txt",'a') as fl:
#     fl.write("this is text data\nthis is next line")

# with open("text5.txt",'r+') as fl:
    # fl.seek(len(fl.read()))
    # fl.write("\nthis is cursor change value and this line should be printed at the last")