s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
print(s1.union(s2))


# update method 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna","udaipur"}
s3 = s1.update(s2)
print(s1)

# intersection 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
print(s1.intersection(s2))

# intersection update 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
s1.intersection_update(s2)
print(s1)


set difference 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
print(s1.symmetric_difference(s2))

# difference 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
print(s1.difference(s2))


# disjoint sets 

s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
print(s1.isdisjoint(s2))

# issuperset  
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
print(s1.issuperset(s2))


#subset 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi"}
print(s2.issubset(s1))

# remove and discard 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
(s1.remove("tokyo"))
print(s1)

(s1.discard("delhi"))
print(s1)

# pop 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
s2.pop()
print(s2)


# # del keyword 

# s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
# s2 = {"tokyo","delhi","raipur","indore","patna"}
# del s1
# print(s1)


# clear method 
s1 = {"tokyo","delhi","mumbai","toronto","nashik"}
s2 = {"tokyo","delhi","raipur","indore","patna"}
s2.clear()
print(s2)



