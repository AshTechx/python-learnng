# try:
#   l1 = []
#   for i in range(10):
#    a = int(input("enter any number"))
#    l1.append(a)
#    print(f" the list of given numbers is as follows  {l1}")
   
#   l2 =[]
#   for i in range (len(l1)):
#     if (l1[i]%2!=0):
#      l2.append(l1[i])
#   print(f"the list of odd numbers are as follows {l2}")
# except ValueError : # type of an error when the datatype entered is not correct example:here the input is integer if someone enters a string value
  
#   print("enter a integer vale")


# second prog 


try:
    n = 34  # secret number between 1 and 50
    attempts = 4                # number of tries allowed

    for i in range(attempts):
        a = int(input("Guess a number between 1 and 50: "))

        if a == n:
            print("Congratulations, guessed correct!")
            break
        elif a < n:
            print("Too low, try again!")
        else:
            print("Too high, try again!")

    else:
        print(f"Sorry, you ran out of attempts. The number was {n}.")

except ValueError:
    print("Please enter an integer value!")
