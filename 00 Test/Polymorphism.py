#Over-loading
# The function is "show" but the behavior is different (based on the number of arguments)
# same functon but no of parameters are different
class A:
    def show(self):
        print("Wellcome")

    def show(self, firstname=''):
        print("Wellcome", firstname)

    def show(self, firstname='', lastname=''):
        print("Wellcome", firstname, lastname)

a = A()
a.show()
a.show('Akash')
a.show('Akashdip', 'Mahapatra')