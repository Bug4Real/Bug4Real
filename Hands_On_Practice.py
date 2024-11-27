#Q1: Calculate 3% discount on the amount entered by the user and display the output as:
The discount on <<amount>> is <<amount after discount>>

#Solution_Q1:
amt = int(input("Enter the amount: "))
dis = amt/100*3
amt_dis = amt-dis
print("The Discount on", amt, "is", amt_dis)