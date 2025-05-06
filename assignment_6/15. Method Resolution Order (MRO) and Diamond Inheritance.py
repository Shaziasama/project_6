class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    pass
d = D()
d.show()  # MRO will determine which show() is called

# You can also print MRO to see the method lookup order
print(D.__mro__)
