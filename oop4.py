#multiple inheritence 

class A:
    def class_a_method(self):
        return 'i\'m class A method'
    def hello(self):
        return 'hello from class A'

class B:
    def class_b_method(self):
        return 'i\'m class B method'
    def hello(self):
        return 'hello from class B'

class C(B,A):
    pass

instace_c = C()

# print(instace_c.class_a_method())
# print(instace_c.class_b_method())
# print(instace_c.hello())


# print(help(C))

# print(C.mro())