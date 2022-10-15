# 6, print table of any number
from unittest import result


number=[2]
for count in range(1, 11):      
    result=list(map(lambda number:number*count,number))
    print(number,'*',count,'=',list(result))    

    