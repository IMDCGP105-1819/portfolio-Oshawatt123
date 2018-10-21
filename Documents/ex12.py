ny_cost = 2000
ak_cost = 790
ve_cost = 154
gl_cost = 65

hotel_cost = 70

rental_cost = 30
temp_rental_cost = 0

# ^^ variable assignment

def hotel_stay_cost(nights):
	return hotel_cost * nights #calculate hotel cost
	
def plane_ticket_cost(city, grade):
	if city == "New York":
		return ny_cost * grade
	elif city == "Auckland":
		return ak_cost * grade # no switch statement so used an elif so switch costs based
	elif city == "Venice":	   # on which city they're visiting
		return ve_cost * grade
	elif city == "Glasgow":
		return gl_cost * grade
	return NULL

def rental_car_cost(days):
	temp_rental_cost = rental_cost * days
	if temp_rental_cost > 7:
		temp_rental_cost -= 50
	elif temp_rental_cost > 3: # doing the if statement like this prevents discount overflow
		temp_rental_cost -= 30
	return temp_rental_cost
	
def total_cost(city, days):
	holiday_cost = 0
	# a lot of int() casts are used to ensure the correct data type is being fed to the function
	holiday_cost += hotel_stay_cost(int(days) -1)
	holiday_cost += plane_ticket_cost(city, int(input("What grade seat would you like on your plane?")))
	holiday_cost += rental_car_cost(int(days))
	return holiday_cost
	
print(total_cost(input("city"), input("Days away"))) # final output