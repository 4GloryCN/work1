class Judger():

    def getdata(self, movie):
        movie.actiontime = input('请输入动作片断数目：')
        movie.romancetime = input('请输入爱情片段数目：')

    def analysis(self, movie):
        if movie.actiontime > movie.romancetime:
            movie.action = True
        else:
            movie.romance = True
