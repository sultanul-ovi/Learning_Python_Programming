print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is you age? "))
    if age < 12:
        print("Pay $5")
    elif age >=12 and age <=18:
        print("Pay $7")
    else:
        print("Pay $12")
        
else:
    print("You can not ride")