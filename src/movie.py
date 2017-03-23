class Movie():

    def __init__(self):
        self.title = ''
        self.action = False
        self.romance = False
        self.action_time = 0
        self.romance_time = 0

    def make_info(self):
        if self.action:
            print("这是动作电影\n")
        elif self.romance:
            print("这是爱情电影\n")
        else:
            print("Something Wrong !\n")
