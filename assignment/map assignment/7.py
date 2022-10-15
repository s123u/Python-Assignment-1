# 7. add two list


l1 = [1, 2, 3]
l2 = [4, 5, 6]
print("Original list:")
print(l1)
print(l2)
result = map(lambda x, y: x + y, l1, l2)
print("\nResult: after adding two list")
print(list(result))