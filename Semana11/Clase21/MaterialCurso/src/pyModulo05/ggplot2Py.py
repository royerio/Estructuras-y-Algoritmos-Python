'''
Created on Feb 5, 2021

@author: freddy
'''
from plotnine.data import economics
from plotnine.data import mpg
from plotnine.data import huron

from plotnine import ggplot, aes, geom_line,geom_point,geom_bar,stat_bin,geom_boxplot

x=(ggplot(economics) + 
  aes(x="date", y="pop") + 
  geom_line() 
)
print(x)
ggplot(mpg) + aes(x="class", y="hwy") + geom_point()

ggplot(mpg) + aes(x="class") + geom_bar()

ggplot(huron) + aes(x="level") + stat_bin(bins=10) + geom_bar()

ggplot(huron)  + aes(x="factor(decade)", y="level")  + geom_boxplot()
  