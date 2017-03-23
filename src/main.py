from user import *
from analyzer import *

print('初始化中······')
analyzer = Analyzer()
user = User()

x, y = analyzer.analysis()
user.measure(analyzer, x, y)
user.exit()
