class User():

    def __init__(self):
        self.prompt1 = '即将开始电影分类分析。（输入quit退出分析，按下Enter键开始分析）\n'
        self.prompt2 = '请输入标准数据（输入0结束输入，按下Enter键开始输入）\n'
        self.order = ''

    def exit(self):
        print("Bye~")

    def measure(self, movie, analyzer, x, y):
        while True:
            self.order = input(self.prompt1)
            if self.order != 'quit':
                analyzer.get_measured_data(movie)
                analyzer.judge(movie, x, y)
                movie.make_info()
            else:
                break
