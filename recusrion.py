# fstrings 

name = "aashiya"
country = "spain"
print(f"my name is {name} and i am from {country}")


# second example 

price = 45.0098
text = f"the price is gonna be {price:.2f}"
print(text)


last_name ="khan"
mid_namme = "firoz"
print(f"my {{last_name }} is {last_name} and my {{mid_name }} is {mid_namme}")



# docstring 

def printnum (n):
  '''
  this funcion is a recursive function used to print numbers 
  '''
  if (n==0):
    return 
  else :
    print(n)
    printnum(n-1)


print(printnum(20))
print(printnum.__doc__) # used to print the doc string 



import this # pep poem given by tim 
















# def numbers (n):
#   if (n==1):
#     return 1
#   else :
#     return n+numbers(n-1)
  

# print(numbers(100))


def print_list (list_1,index=0):
  if (index >= len(list_1)):
    return 
  print(list_1[index])
  print_list(list_1,index +1)



list_1 = ["apple","mango","banana"]
print_list(list_1)