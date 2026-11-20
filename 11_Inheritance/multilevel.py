class A:
    a = 1

class B(A):
    b = 2

class C(B):
    c = 3



o = C()
print(o.a, o.b, o.c)