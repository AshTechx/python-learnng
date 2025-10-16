# merging two tuples sort into an ascending order 
tuple_1 = (5,2,9)
tuple_2 = (1,7,3)
tuple_3 = tuple_1 + tuple_2
new_list = list(tuple_3)
new_list.sort()
print(new_list)

# counting the occurrences of the element 
my_list = [1,2,2,3,4,2,5]
counting = my_list.count(5)
print(counting)

#finding index for the elements 
my_list_2 = ["apple","banana","guava","pineapple"]
indexing = my_list_2.index("pineapple")
print(indexing)


#inserting the element at the index 
my_list_3 = [10,20,30,40]
my_list_3.insert(2,25)
print(my_list_3)


# converting tuple to list and reverse 
my_tup = (1,2,3,4,5)
new_list = list(my_tup)
new_list.reverse()
print(new_list)
print(my_tup)
