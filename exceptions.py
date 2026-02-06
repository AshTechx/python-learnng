# bank example 
class InsuffiecientfundError (Exception):
  def __init__(self):
    super()._init__("insufficient balance")


balance = 2400000
try :
  withdrawal = int (input("enter the withdrawal amount"))
  if(withdrawal>balance):
    raise InsuffiecientfundError
  else:
    print("withdrawal successful ")
except InsuffiecientfundError as e :
  print(e)

password validator example 
class WeakpasswordError (Exception):
  def __init__(self):
    super().__init__("weak password not acceptable ")

try :
  password = input ("enter the password")
  if (len(password)<8):
    raise WeakpasswordError
  else:
    print("good password choice")
except WeakpasswordError as e:
  print(e)


class InvalidQuantityError (Exception):
  def __init__(self):
    super().__init__("invalid Quantity")

def func1 ():
  try:
   cart = []
   item = input("enter the item name")
   qty = int(input("enter the quantity"))
   if(qty<0):
    raise InvalidQuantityError
   else:
    cart.append((item,qty))
  except InvalidQuantityError as e :
    print(e)
  finally:
    print("cart process finished ")

x = func1()


  


  
