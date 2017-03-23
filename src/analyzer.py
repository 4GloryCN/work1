import json

class Analyzer():

    def judge(self, x, y):
        action_time = int(input('请输入动作片断数目：'))
        romance_time = int(input('请输入爱情片段数目：'))

        if (action_time - x) - (romance_time - y) > 0:
            print("这是动作电影\n")
        else:
            print("这是爱情电影\n")

    def analysis(self):
        print("数据分析中······\n")

        action_count = 0
        romance_count = 0
        action_sum = 0
        romance_sum = 0

        with open('./resource/movies.json') as f_obj:
            data = json.load(f_obj)

        for movies in data['movies']:
            if movies['type'] == 'Action':
                action_sum += (movies['kicks'] - movies['kisses'])
                action_count += 1
            else:
                romance_sum += (movies['kisses'] - movies['kicks'])
                romance_count += 1

        return action_sum/action_count, romance_sum/romance_count
