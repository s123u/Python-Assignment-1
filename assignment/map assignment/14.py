# This time using filter() and list() functions filter all the positive integer in the string.


num = [12, 1, 0, -2, 2, -8]
Result = list(filter(lambda x: x >0, num))
print(num)
print(Result)