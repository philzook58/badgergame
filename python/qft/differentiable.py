

class Differentiable:
    def __init__(self, func, deriv=None):
        self.func=func
        self.deriv = deriv
    def __mul__(self, b):
        a = self
        return Differentiable(lambda x: a.func(x) * b.func(x),deriv = lambda x: a.func(x) * b.deriv(x) +a.deriv(x) * b.func(x))
    def __add__(self, b):
        a = self
        return Differentiable(lambda x: a.func(x) + b.func(x), deriv = lambda x: a.deriv(x) + b.deriv(x))
    def __pow__(self, b):
        a= self
        return Differentiable(lambda x: a.func(x)**b, deriv = lambda x: b*a.deriv(x)* a.func(x)**(b-1))
    def compose(self, b):
        a = self
        return Differentiable(lambda x: a.func(b.func(x)), lambda x: b.deriv(x)* a.deriv(b.func(x)))
import math

cos = Differentiable(math.cos,lambda x : -1*math.sin(x))
sin = Differentiable(math.sin, math.cos)
x = Differentiable(lambda x: x, lambda x: 1)

print (x**2).deriv(2)
print (x**2).func(2)
print (x+(x**2)).deriv(3)

chain = (x**2).compose(x**2)
print chain.deriv(2)
