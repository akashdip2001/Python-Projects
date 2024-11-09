# #Single Threading
# from time import sleep
# class A:
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)

# class B:
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)

# t1 = A()
# t2 = B()

# t1.run()
# t2.run()

# # output:
# # Hello
# # Hello
# # Hello
# # Hello
# # Hello
# # Hi
# # Hi
# # Hi
# # Hi
# # Hi

# #Multi Threading
from time import sleep
from threading import Thread

class A(Thread):  # Inherit from Thread
    def run(self):  # Correctly define the run method
        for i in range(5):
            print("Hello")
            sleep(1)

class B(Thread):  # Inherit from Thread
    def run(self):  # Correctly define the run method
        for i in range(5):
            print("Hi")
            sleep(1)

# Create instances of A and B
t1 = A()
t2 = B()

# Start the threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# output:
# Hello
# Hi
# Hello
# Hi
# Hello
# Hi
# Hello
# Hi
# Hello
# Hi
#### **Multi Threading:** Run at same time using threads (parallel execution)
