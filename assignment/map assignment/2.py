# 2 separate even odd number from given list

from unittest import result


num=[1,2,3,4,5,6,7,8,9,0]
result=list(map(lambda num:num%2==0,num))
print(list(result))