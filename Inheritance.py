#Inheritance -Inherits the properties of Base class
#It involves MRO -Method Resolution order and diamond Problem solution using c3 Linearization
#Method Overloading is not supported by Py but Method overriding defines redefining the methods by inheriting the class 
class A():
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        super().show()
class C(A):
    def show(self):
        print("C")
        super().show()
class D(B,C):
    def show(self):
        print("D")
        super().show()
d=D()
d.show()
print(D.mro())
