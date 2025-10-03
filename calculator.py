class Calculator():
    def add(self,a,b):
        return a+b
    def subtract(self,c,d):
        return c-d
    def multiply(self,e,f):
        return e*f
    def divide(self,g,h):
        if h==0:
            raise ValueError("You can not divide by zero")
        return g/h
    