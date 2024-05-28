# Python functions

# Example 1: Define a function that takes a log as its input and returns a string 

def display_investigation_message():
  print("Investigate activity")
  application_status = "potential concern"
  email_status = "okay"
if application_status == "potential concern":
  print("application_log: ")
  display_investigation_message()
if email_status == "potential concern":
  print("email log: ")
  display_investigation_message()

def list_to_string():
	username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
  print(sorted(username_list))
	sum_variable = ""
	for i in username_list:
		sum_variable = sum_variable + i + ", "
	print(sum_variable)

# Output:
# list_to_string()
# elarson, bmoreno, tshah, sgilmore, eraab, gesparza, alevitsk, wjaffrey,

def remaining_login_attempts(maximum_attempts, total_attempts):
	return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(3, 3)
if remaining_attempts <= 0:
	print("Your account is locked")

def analyze_logins(username, current_day_logins, average_day_logins):
	print("Current day login total for", username, "is", current_day_logins)
	print("Average logins per day for", username, "is", average_day_logins)
	if average_day_logins > 1:
		login_ration = current_day_logins / average_day_logins
	print(username, "logged in", login_ratio, "times as much as they do on an average day.)

analyze_logins("ejones", 9, 7)

approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users)
approved_users = ",".join(approved_users)
print("after .join():", approved_users)

def login_check(login_list, current_user):
	counter = 0 
	for i in login_list:
		if i == current_user:
				counter = counter + 1
		if counter >= 3
			return "You have tried to login three or more times. Your account has been locked"
		else:
			return "You can log in!"

login_check(usernames, "eraab")
