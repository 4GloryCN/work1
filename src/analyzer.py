from movie import *
import json

class Analyzer():

    def get_origin_data(self):
        content = []
        print('数据读取中······')

        with open('./resource/movies.json') as f_obj:
            data = json.load(f_obj)

        for movies in data['movies']:
            movie = Movie()

            movie.title = movies['title']
            movie.action_time = movies['kicks']
            movie.romance_time = movies['kisses']
            if movies['type'] == 'Action':
                movie.action = True
            else:
                movie.romance = True

            content.append(movie)

        return content

    def get_measured_data(self, movie):
        movie.action_time = int(input('请输入动作片断数目：'))
        movie.romance_time = int(input('请输入爱情片段数目：'))

    def analysis(self, content):
        print("数据分析中······\n")

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