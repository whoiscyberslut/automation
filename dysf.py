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
