# Using filter() function filter the list so that only negative numbers are left.


nums = [4, 1, 0, -2, 2, -8]
new_nums = list(filter(lambda x: x <0, nums))
print(nums)
print(new_nums)