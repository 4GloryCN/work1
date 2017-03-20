from movie import *

from judger import *


class Observer():

    def __init__(self):
        self.prompt = '即将开始电影分类分析。（输入quit退出分析，按下Enter键开始分析）\n'
        self.order = ''
        self.movie = Movie()
        self.judger = Judger()

    def on(self):
        while True:
            self.order = input(self.prompt)
            if self.order != 'quit':
                self.judger.getdata(self.movie)
                self.judger.analysis(self.movie)
                self.movie.makeinfo()
            else:
                break

    def off(self):
        print("Bye~")
