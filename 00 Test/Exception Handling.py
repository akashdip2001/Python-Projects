# try:
#     x = 1 / 0
# except ZeroDivisionError as e: # ZeroDivisionError is a subclass of Exception
#     print(f"Error: {e}")

a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))

try:
    x = a/b
    print("The ans is : ",x)
except:
    print("can't division by zero")
else:
    print("Thanks")

# Enter 1st no: 1
# Enter 2nd no: 0
# can't division by zero