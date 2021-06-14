'MRO -> Method Resolution Order'
"""
MRO is a concept used in inheritance. 
It is the order in which a method is searched for in a classes hierarchy 
and is especially useful in Python because Python supports multiple inheritance.
"""


class A:
    def method(self):
        print("A.method() called")


class B:
    def method(self):
        print("B.method() called")


class C(A, B):
    pass


c = C()
c.method()

"""
The MRO for this case is:
C -> B -> A
The method only existed in A, where it was searched for last

The first method it will get it in its parent class
"""


# 2nd case
class A:
    def method(self):
        print("A.method() called")


class B:
    def method(self):
        print("B.method() called")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.method()

"D -> C -> A -> B"


class D(B, C):
    pass
    "B cannot be defined before C , because B is super class of C"
