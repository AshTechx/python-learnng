# #shorthand if else for finding even numbers 

num = int(input("enter the number"))
print("invalid") if(num==1 or num==0) else print("even") if (num%2==0) else print("odd")

# shorthand if else for finding valid age 
age = int(input("enter the age"))
print("invalid age ") if (age <=0) else print("eligible") if(age>=18) else print("ineligible")


#enumerate function 
def pos_finder (l):
  for index, i in enumerate(l):
    print("the index of the list is",index,i)


l = ["apple","banana","cherry"]
pos_finder(l)

#enumerate function for index starting from 1 
def pos_finder (l2):
  for ind, i in enumerate(l2,start=3):
    print("the index of the list is",ind,i)


l2 = ["rahul","priyu","sawant"]
pos_finder(l2)

# practise ques code language 
sentence = input("enter the lines")
l2 = sentence.split()
for i in l2:
  if (len(i)==2):
    new = i[1]+i[0]

    print(new)
  elif (len(i)>=3):
    new_word =i[1:]+i[0]
    latest = "alr"+new_word+"alr"
    
    print(latest)
  
  else:
      print(i)


