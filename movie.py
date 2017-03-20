class Movie():

    def __init__(self):
        self.action = False
        self.romance = False
        self.actiontime = 0
        self.romancetime = 0

    def makeinfo(self):
        if self.action:
            print("这是动作电影\n")
        elif self.romance:
            print("这是爱情电影\n")
        else:
            print("Something Wrong !\n")
