# # Parameteriged constructor
# class A:
#     def __init__(self,age,name,address):
#         address="Kolkata" #optional
#         print(age," ",name," ",address)

# obj=A(10,"Akash",None)



# # use those members in only inside the class
# class A:
#     a=10   # Public member
#     _b=20  # Protected member
#     __c=30 # Private member

#     print(a," ",_b," ",__c) 

# #output:10   20   30




# class A:
#     a = 10   # Public member
#     _b = 20  # Protected member
#     __c = 30 # Private member
#     print("In same class:",a," ",_b," ",__c) 
#     # Constructor to print values inside the class
#     def show(self):
#         print("Inside the same class members:", self.a, self._b, self.__c)

# # Creating an object of class A
# obj = A()
# obj.show()
# print("Outside the class:", obj.a, obj._b, obj.__c)


class A:
    a = 10   # Public member
    _b = 20  # Protected member
    __c = 30 # Private member

# Creating an object of class A
obj = A()
print("Outside the class:", obj.a, obj._b) #output:10   20   30
print("Outside the class:", obj.a, obj._b, obj.__c) #output: Error