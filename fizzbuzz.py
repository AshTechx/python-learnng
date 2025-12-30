# fizzbuzz 

number = int(input("enter the number"))
ans = []
for i in range(1,number+1):
  if (i%3==0 and i%5==0):
    ans.append("Fizz")
  
  elif (i%3==0 ):
    ans.append("Fizzbuzz")
  elif  (i%5==0):
    ans.append("Buzz")
  else:
    ans.append(str(i))
  
  
print(ans)
