from movie import Movie

class Analyzer():
    def __init__(self):
        self.flag = ''

    def get_origin_data(self):
        movie = Movie()

        movie.action_time = int(input('请输入动作片断数目：'))
        movie.romance_time = int(input('请输入爱情片段数目：'))
        self.flag = input('请输入电影类别：（A or R）')

        if self.flag == 'A':
            movie.action = True
            movie.romance = False
            return movie
        elif self.flag == 'R':
            movie.romance = True
            movie.action = False
        else:
            print("输入错误请重新输入")
            return None

        return movie

    def get_measured_data(self, movie):
        movie.action_time = int(input('请输入动作片断数目：'))
        movie.romance_time = int(input('请输入爱情片段数目：'))

    def analysis(self, content):
        print("数据分析中······\n")

        content.remove(None)
        action_count = 0
        romance_count = 0
        action_sum = 0
        romance_sum = 0

        for i in content:
            if i.action:
                action_sum += (i.action_time - i.romance_time)
                action_count += 1
            else:
                romance_sum += (i.romance_time - i.action_time)
                romance_count += 1

        return action_sum/action_count, romance_sum/romance_count

    def judge(self, movie, x, y):
        if (movie.action_time - x) - (movie.romance_time - y) > 0:
            movie.action = True
        else:
            movie.romance = True