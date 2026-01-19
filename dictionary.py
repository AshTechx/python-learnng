info = {"name":"aashiya","age":20,"city":"Nashik","blood group":"b positive","lastname":"khan"}
print(info)
print(info["name"])
print(info["age"])
print(info.keys())
print(info.values())
print(info.items())

for value in info.keys():
  print(info[value]) # this will print the values in the key 


for key,value in info.items():
  print(f"the values for the {key} are as follows {value}")
  #  printinh both the key and values using looping statamenets 

# dictionary methods 
ep1 = {122:34,76:87,9:78,45:56}
ep2 = {23:45,89:56,34:57,789:78}
ep1.update(ep2)
print(ep1)

info.clear()
print(info)  # used to clear the dictionary 

ep1.pop(122) # removes the given element 
ep1.popitem() # removes the last element 
del ep1[23]
print(ep1)

# del ep1 will delete the entire dictionary 