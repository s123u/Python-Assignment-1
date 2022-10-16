# Using filter function, filter the even numbers so that only odd numbers are passed to the new list.

lst1=[1,2,3,4,5,6,7,8,9,10]

lst2=list(filter(lambda x: x%2 == 1, lst1))

print(lst2)
