
# using simple way 
# name = (input("enter your name"))
# time = int(input("enter the time"))
# if(time >= 5 and time<=12):
#   print("good morning user ",name)
# elif(time>=13 and time<=16):
#   print("good afternoon user",name)
# elif(time>=17 and  time<=19):
#   print("good evening user ", name)
# elif(time>=20  and time<=24):
#   print("good night user",name)
# else:
#   print("wrong time is put ")


import time
timestamp = int((time.strftime("%H%M%S")))
if(timestamp >=50000 and timestamp<=120000):
  print("good morning")
elif(timestamp >=130000 and timestamp<=160000):
  print("good afternoon")
elif(timestamp>=170000 and timestamp<=190000):
  print("good evening user")
elif(timestamp>=200000 and timestamp<=240000):
  print("good night user")
else:
  print("wrong time")

print(time.strftime("%H:%M:%S"))