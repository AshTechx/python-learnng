# m = int(input("enter smtg "))
# n = int(input())
# list_1 =[]
# for i in range (m+1):
#   for j in range (n+1):
#     if (i+j) %3!=0:
#       list_1.append([i,j])
# print(list_1)


# list comprehension way of writing the above code is as follows 
m = int(input("enter smtg "))
n = int(input("enter second value "))
my_list = [[i,j] for i in range (m+1) for j in range (n+1) if (i+j)%3!=0  ]
print(my_list)