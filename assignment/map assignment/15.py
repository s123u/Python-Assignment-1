# Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.[Try using map inside filter]

l1 = [-10, 21, 4, -45, -66, 93, -11] 
 
Result = list(filter(lambda x: (x < 0), l1))
 
print("Negative numbers ", Result)