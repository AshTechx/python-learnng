#numbers from 1-100

# i =1
# while i<=100 :
#   print(i,"numbers from 1 to 100")
#   i+=1

# numbers 100 to 1
# count = 100
# while count>=1:
#   print(count,"numbers from 100 to 1")
#   count = count -1
 
# multiplication table 
# var_1 = int(input("enter any number"))
# i=1
# while i<=10:
#   mul = var_1 *i
#   print(input,"*",i,"=",mul)
#   i+=i

# square nos 

# num =1 
# while num<=10:
#   square = num*num
#   print("the square of",num,"is",square )
#   num+=1

# printing over a list 

# lis_1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index < len(lis_1):  
#     print(lis_1[index])
#     index += 1


# search for the number 
num = (1,4,9,16,25,36,49,64,81,100)
i=0
while i<len(num):
  var_1 = int(input("enter the number"))
  if var_1!=num[i]:
    print("no the number is  not present",num[i])
    i+=1
  else:
    print("good one correct guessed ")
    break

  

