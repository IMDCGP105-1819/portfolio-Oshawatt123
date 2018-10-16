annual_salary = float(input("Please input your annual salary"))
portion_saved = float(input("Please input the portion of salary to be saved every month (in decimal form e.g: 0.1 for 10%)"))
total_cost = float(input("What is the cost of your dream home?"))
semi_annual_raise = float(input("Enter your semi-annual salary raise! (in decimal form e.g: 0.1 for 10%)"))
# ^^ casting to float so the calculations work
deposit = total_cost * 0.2
months_saving = 0
current_savings = 0
interest = 0.04
while current_savings < deposit:
	current_savings += (annual_salary/12) * portion_saved # monthly salary portion added to savings
	current_savings += current_savings*interest/12 # monthly interest added to savings
	print("Month: " + str(months_saving) + " Current savings: " + str(current_savings)) # debug log
	months_saving += 1 # month count
	if months_saving%6 == 0:
		annual_salary += annual_salary*semi_annual_raise
print(months_saving) # the wrong answer 