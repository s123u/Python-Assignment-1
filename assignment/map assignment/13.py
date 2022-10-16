# Using filter() and list() functions and .lower() method filter all the vowels in a given string.


l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst = list(filter(lambda x: True if x.lower() in "aeiou" else False, l))
print(lst)
