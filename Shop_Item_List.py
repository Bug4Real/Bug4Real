#Define the items of the shop
item_list = {
  'TicWatchPro': 8999,
  'Flipper Zero': 50199,
  'Rubber Ducky': 18999,
  'Hackypi': 2999,
}

#Great
print("Welcome to the HACKERS shop!")
print("Here is the item list:\nTicWatchPro: Rs8999\nFlipper Zero: Rs50199\nRubber Ducky: Rs18999\nHackypi: Rs2999")

order_total = 0
#5999+59999=65998

item_1= input("What is the first item you want to buy? ")
if item_1 in item_list:
  order_total += item_list[item_1]
  print("Your item has been added to your order. ")

else:
  print("Sorry, this item is currently not available. ")

another_order = input("Do you want to buy another item? (Yes/No): ")
if another_order == "Yes":
  item_2 = input("What is the second item you want to buy? ")
  if item_2 in item_list:
    order_total += item_list[item_2]
    print("Your item has been added to your order. ")
  else:
    print("Sorry, this item is currently not available. ")
  print("Thank you for shopping with us! ")
  print("The total amount you have to pay is Rs", order_total)
  