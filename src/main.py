from user import *
from movie import *
from analyzer import *

print('初始化中······')
movie_0 = Movie()
analyzer = Analyzer()
user = User()

content = analyzer.get_origin_data()
x, y = analyzer.analysis(content)
user.measure(movie_0, analyzer, x, y)
user.exit()
