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

# second question practice 

def oddNumber():
    a = int(input("Enter the start number: "))
    b = int(input("Enter the end number: "))
    count = 0
    for i in range(a, b):
        if i % 2 != 0:
            count += 1
    return count

var_1 = oddNumber()
print(var_1)


#third practice question 
str1 = input("enter the string")
half = round(len(str1)/2)
for i in range (half):
  print(str1[i])


# fourth question
def capitals(str):
  for i in str:
    if(i.isupper()==True):
      print(i)


capitals("AaShiya")