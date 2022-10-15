# 8 Convert all float digits into integer using built in function from given list.
from unittest import result


l=[1.0,2.1,3.2,4.3,6.4,0.5]
result=map(lambda l:int(l),l)
print(list(result))