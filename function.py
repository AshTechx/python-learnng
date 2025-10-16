# applying the discount for the price 
def calculate_discount (price,discount_percent):
  discount = price * (discount_percent)/100
  final_price = price - discount
  return final_price


answer = calculate_discount(100,10)
print(answer)



