class A:
    def __init__(self):
        print("COnstructor of A")
    a = 1

class B(A):
    def __init__(self):
        print("COnstructor of B")
    b = 2

class C(B):
    def __init__(self):
        super().__init__()
        print("COnstructor of A")
    c = 3



o = C()
print(o.a, o.b, o.c)