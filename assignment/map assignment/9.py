# 9 reverse given set


lst = [10, 11, 12, 13, 14, 15]


result=map(lambda lst:lst.reverse(),lst)
print("Using reversed() ", set(reversed(lst)))