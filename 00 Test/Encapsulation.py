class A:
    _a=10 # protected #data
    __b=20 # private
    def dis_fun(self): #function, ----> &, data + Function = Encapsulation
        print(self._a)
        print(self.__b)

x=A() #object
x.dis_fun()

print("Outside of class ",x._a)
print("Outside of class ",x.__b)