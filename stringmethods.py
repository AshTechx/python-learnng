# lenght of the string 
fruit = "mango"
print(len(fruit))
# slicing of the strings 
fruit = "mango"
print(fruit[0:3])
print(fruit[:4])
print(fruit[1:])
print(fruit[-1:-3])
# here is the above statement the interpreter interprets as print(fruit[len(fruit)-1:len(fruit)-3])


#rstrip()method : this method is used to remove any characters in the end 

str1 = "hello this is aashiya!"
print(str1.rstrip("!"))

# replace 
str2 = "aashiya is writing"
print(str2.replace("aashiya","priyanshu"))

#split method 
str3 = "aashiya is a good girl"
print(str3.split(" ")) # here this only splits if the respective string has spaces 


#capitalize 
str4 = "ashraf"
print(str4.capitalize()) # this is used to capitalize the first letter in the string 

# center 
str5 = "welcome to the console"
print(str5.center(50))

# count 
str6 = "aashiya is sassy"
print(str6.count("s"))

#endswith 
str7 = "lets check is code ends with !"
print(str7.endswith("!"))

# find 

str8 = "aashiya is good girl she is writing the code right now"
print(str8.find("is"))  # this returns the index of the  searched value & if the valuse is not available it will give the value as -1


str9 = "aashiya"
print(str9.index("y"))

str10 = "WelcometoConsole" # returns false if the string has spaces if it has special characters and if it has symbols 
print(str10.isalnum())

str11 = "aashiya"
print(str11.isalpha())

str12 = "Kalpana"
print(str12.islower())

str13 = "this is on the console an this "
print(str13.isprintable()) # this will return false if the string has any escape sequence character example 

str14 = "this is aashiya \n hello "
print(str14.isprintable())

str15 = "hello guys console "
print(str15.isspace()) # returns true if there are only spaces \t also works 

str16 = "World Health Organization"
print(str16.istitle())
# returns true only if the string has capital letter in the start 
