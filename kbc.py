# kaun banega crorepati 

list_1 = ["what is the capital of india","what is the national bird of india","what is the national animal of india","who is the prime minister of india"]
list_2 = ["delhi","peacock","tiger","modi"]
total_money = 0

for i in  range(len(list_1)):
    print(list_1[i])
    user_ans = input("enter the answer")
    if i==0 and user_ans != list_2[0]:
        print("sorry out of game")
        break
    elif user_ans == list_2[i]:
        total_money += (i+1)*100
        print("yess you won",total_money)
        
    else:
        total_money -= 100
        print("you lost rs 100  ")
        print()
print("you total winnings",total_money)