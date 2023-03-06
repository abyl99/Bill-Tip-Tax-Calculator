#define and set variables from user (cast to a float)
bill = float(input('How much is your meal?'))
tax = float(input('What is the sales tax (percentage)?'))
tip = float(input('How much will you tip (percentage)?'))
            
#calculate and add tax amount
tax_amount = (bill*tax)/100 #calculate tax amount
total = bill + tax_amount #add tax amount to final bill 

#calculate and add tip amount
tip_amount = (total*tip)/100 #calculate the tip amount
total = total + tip_amount #add tip amount to finall bill 

#round the total to 2 decimal places
total = round(total,2) #round the total amount

#print the final amount with tax and tip
print('Your total bill is $ ', total) 
