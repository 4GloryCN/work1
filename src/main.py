from user import *
from movie import *
from analyzer import *


movie = Movie()
movie_0 = Movie()
analyzer = Analyzer()
user = User()
content = []

user.startup(content, analyzer)
x, y = analyzer.analysis(content)
user.measure(movie_0, analyzer, x, y)
user.exit()
