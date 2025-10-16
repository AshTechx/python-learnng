def discount (*number):
  for i in number:
    if(i>50):
      final_price = i - i*(10/100)
      print("discount applied",final_price)
    else:
      print("not applied")
      

discount(10,100,60,30)