class Father:
    def sky(self):
        print("sky is Blue")

class Son(Father):
    def grass(self):
        print("grass is Green")

#obj = Son()
X = Son() # X is an object of class Son
X.sky() # method of class Father (other class)
X.grass() # method of class Son (own class)