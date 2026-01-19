try:
  l1 = []
  for i in range(10):
   a = int(input("enter any number"))
   l1.append(a)
   print(f" the list of given numbers is as follows  {l1}")
   l2 =[]
   for i in range (len(l1)):
    if (l1[i]%2!=0):
     l2.append(l1[i])
   print(f"the list of odd numbers are as follows {l2}")
except ValueError : # type of an error when the datatype entered is not correct example:here the input is integer if someone enters a string value
  
  print("enter a integer vale")
