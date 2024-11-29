#Q1: Calculate 3% discount on the amount entered by the user and display the output as:
The discount on <<amount>> is <<amount after discount>>

#Solution_Q1:
amt = int(input("Enter the amount: "))
dis = amt/100*3
amt_dis = amt-dis
print("The Discount on", amt, "is", amt_dis)


#Q2: Ganesh has a grassland on his farm house in a perfect circular shape. Accept circumference of the grassland and calculate its area. Circumference is double of radius and area of circle is calculated as 3.14*radius*radius

#Solution_Q2:
circumference = float(input("Enter the circumference of the grassland: "))
radius = circumference/2 #radius is half of the circumference
area = 3.14 * radius * radius
print("The area of the grassland is", area)


#Q3: Accept the height of the user in feet and inches separated by decimal. Example: 60.7 means 5 feet 7 inches. Then display the height in feet and inches separately. Example: Feet=5, Inches=7.0

#Solution_Q3:
height = input("Enter your height in feet and inches separated by decimal: ")
feet, inches = map(int, height.split("."))
print( "Feet:", feet/12, "\nInches:", inches)