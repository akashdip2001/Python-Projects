# count = 0
# while count < 5:
#     print(count)
#     count += 1

password = "123XYZ"
user_password = input("Enter the pass: ")

while password != user_password:  # Loop until the password matches
    user_password = input("Enter the pass: ")  # Prompt user again

print("Unlocked !!")
