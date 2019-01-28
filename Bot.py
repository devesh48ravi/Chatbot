#Hello Friends,all functions of the chatbot will be written here:-
def first_initailze():
	print("Hello, I am your friendly chatbot here with you to chat\n")
	first_attempt = input("So from where we start\n")
#Add the questions here:-
	if "What is your name" == "What is your name":
		print("My name is Munna.")
		response = input("Wanna to ask a new question[Y|N]\n")
		#OR here is for different  options
		if "Y"or"y"or"Yes"or"yes" == response :
			return again()
		else:
			return "Bye"
	else:
		print("Sorry,our engineers are working on this question\n ")
		new_one = input("Please can u repeat that question that you asked our technicians will find it")
#here it defines the again function
def again():
	first_attempt = input("So ask something else\n")
	#Here also "or" for different options
	if "what is your age"or"What is your age" == first_attempt:
		print("My age depends from the Date I was made\n")
		today_date = input("So if we calculate from that so you have to enter today Date (Ex\"28\")\n")
		current_month = input("Enter current month (Ex\"1 for Jan and 2 for Feb\")\n")
		current_year = input("Enter current year (Ex\"2019\")\n")
		print(age(today_date, current_month, current_year))





def age(today_date, current_month, current_year):
	diffrence_between_year = int(current_year) - 2019
	diffrence_between_month = int(current_month) - 1
	diffrence_between_days = int(today_date) - 27
	age = diffrence_between_year,diffrence_between_month,diffrence_between_days
	return age
print(first_initailze())