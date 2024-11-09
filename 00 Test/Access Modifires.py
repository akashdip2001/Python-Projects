# class Car:
#     def __init__(self):
#         self.van = "Public Variable"      # Public: accessible anywhere
#         self._van = "Protected Variable"  # Protected: meant for internal use
#         self.__van = "Private Variable"   # Private: name mangling applied

# car = Car()
# print(car.van)        # Accessible
# print(car._van)       # Accessible but discouraged
# print(car._Car__van)  # Accessing via name mangling (discouraged)


#create a another class - B, 🛩️ Inherit class - A 
class A: #Parent class
    a = 10   # Public member
    _b = 20  # Protected member
    __c = 30 # Private member

class B(A): # Child class
    def show(self):
        print("Inherit class:", self.a, self._b)

obj=B()
obj.show()