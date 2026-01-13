
# prac ques 1
list_1 = [2,4,5,6,6,7,8]
for i in list_1:
  if (i==7):
    print("7 found")
    break
else:
  print("ntg found ")

 # prac ques2
for i in range (6):
  if (i%2==0):
    print("even number found")
  else:
    print("odd number")


# password attempts 
# user = input("enter the password")
# password = "python123"
for i in range (3):
  user = input("enter the password")
  password = "python123"
  if (user == password):
    print("access given")
    break
else :
  print("acess denied ")


  
