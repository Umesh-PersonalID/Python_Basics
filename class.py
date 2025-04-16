#everything in python is object

class computer:
    #whenever we create the object, this init method will call automatically
    def __init__(self,ram = "4GB",cpu="i3"):
        self.x = ram
        self.y = cpu

    def configure(self):
        print("my configuration is ", self.x, "ram memory", self.y, "CPU")
        pass


com1 = computer("8GB","i7")
com2 = computer()
com1.configure()
com2.configure()

#everytime we create the object it will aloocated to new heap memory