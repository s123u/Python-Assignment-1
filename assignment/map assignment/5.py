# 5. eliminate duplicate letter from the string 
from collections import OrderedDict
from os import remove
from unittest import result

def remove_duplicate(s): 
    return "".join(OrderedDict.fromkeys(s))

# test
s=["abcfgbsca"]
result=map(remove_duplicate,s)
print("before",s)
print("after",list(result))
