# 4. print square root of the given numbers

def num(n):
  return n * n
nums = [1,2,3,4,5,6]

result = map(num, nums)

print(list(result))