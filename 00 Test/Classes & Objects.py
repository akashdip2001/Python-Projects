# #with default python constructor
# class A:
#     age=10
#     print(age)
# obj=A()
# obj2=A()
# # with default python constructor, you have to print every time to get the value of age


# # #create a class with constructor
# class A:
#     def __init__(self): # self is default reference parameter which refers to the object
#         age=10
#         print(age)
# obj=A()
# obj2=A()
# # if you create your own constrictor, you must have an object.

# #call document object in side a function
# class A:
#     "Akashdip Mahapatra 01" #The document must in 1st line.
#     age = 10
#     "Akashdip Mahapatra 02" #output: None
#     def fun(self):
#         "Akashdip Mahapatra 03"
#         name="Akash coding"
#         print(self.age)
#         print(name)
# obj=A()
# print(obj.age) # call through object
# print(A.age) # call through class 
# print(obj.__doc__)
# obj.fun()
# print(obj.fun.__doc__) # call through object

# with default python constructor
class A:
    def fun(self,age,name,address):
        print(age," ",name," ",address)

obj=A()
obj.fun(10,"Akash","Kalkata")

# without default python constructor
class A:
    def __init__(self,age,name,address):
        print(age," ",name," ",address)

obj=A(10,"Akash","Kalkata")
        
