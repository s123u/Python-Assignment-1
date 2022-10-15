# print all the string in the lower case from the given tuple



def mytuple(s):
  return  str(s).lower()
 
mystr =["MY NAME IS SUJAL"]

result = map(mytuple, mystr)
print(tuple(result))