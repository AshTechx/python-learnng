def chceking (name,email,age,skills):
  '''
 this function is regarding the user validation using python 
  '''
  if (age <18):
    print("you are not eligible ")
  
  if ('@' not in email or '.' not in email):
   print("not a valid email")
  else:
    print("absolutely fine ")
  
  
  for i in skills:
   print(f"the skills are as follows {{first skill}} and {{other skills }} ",i)



new = chceking("aashiya","aashiyakhan403@gmail.com",20,["sql","python","html"])
print(new)