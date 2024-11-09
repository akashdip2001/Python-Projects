# # default constructor:
# class A:
#     def __init__(self):
#         print("This is default constructor")

# obj=A()




# class A:
#     name="Akashdip" #create a class variable (member)
#     def __init__(self):
#         print(self.name)

# obj=A()




class A:
    name="Akashdip"
    age=20

    def __init__(self):
        address="Kolkata" #member (local variable) inside constructor
        print(self.name)
        print(address) #No need to use self with local variable

    #normal methode
    def show(self): 
        print(self.age)

obj=A()
obj.show() #manually call the method
        