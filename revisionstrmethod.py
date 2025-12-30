# # string methods 
# a = "harry"
# print(a.lower())

# a = "hello!"
# print(a.rstrip("!"))

# b = "hello im aashiya and he is priyanshu"
# print(b.replace("aashiya","maladevi"))

# c = "silver spoon is there"
# print(c.split(" "))

# d = "hey there"
# print(d.capitalize())

# e = "we are coding right now"
# print(e.center(40))

# f = "harry"
# print(f.count("r"))

# g = "we are practising!"
# print(g.endswith("are",1,6))


# h = "we will check and we will answer"
# print(h.index("we"))


# i= "the4password6is5Aashiya007"
# print(i.isalnum())

# j = "none"
# print(j.islower())

# k = "i am eating"
# print(k.capitalize())

# l = "Hello Guys I"
# print(l.istitle())

# m = "hello\niam aashiya\nyk"
# print(m.isprintable())





# # if-else questions practice 
# username = input("enter the username")
# password = input("enter the password")
# if (username == "admin" and password =="1234"):
#   print("login successful")
  
# student grade checker 

marks = int(input("enter the marks"))
if (marks>=90):
  print("Grade A")
elif (marks>=79 and marks<=89):
  print("Grade B")
elif(marks>=50 and marks<=70):
  print('gardeC')
else:
  print("failed")