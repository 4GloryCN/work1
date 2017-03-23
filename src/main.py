from user import *
from movie import *
from analyzer import *

print('初始化中······')
movie_0 = Movie()
analyzer = Analyzer()
user = User()

x, y = analyzer.analysis()
user.measure(movie_0, analyzer, x, y)
user.exit()
