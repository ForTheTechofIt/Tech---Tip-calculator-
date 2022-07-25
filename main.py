

print('Welcome to the tip calculator!')
bill = float(input("What was the total bill? $"))
tip = int(input('How much tip would you like to give? 10, 12, or 15 etc. ? ')) 
split = int(input('How many people will be splitting the bill? '))

finaltip = round(bill * (tip / 100), 2) #percentages are numbers divided by 100 ie. 40% is .40 or, 40/100
print(f"Total tip amount is ${finaltip}")
finalbill = round(finaltip + bill, 2)

finalsplit = "{:.2f}".format(finalbill / split , 2) #formatting added to make sure there were 2 decimal places after the dollar amount.

print(f"Each person should pay: ${finalsplit}")
#