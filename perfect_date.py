# Create a string that holds a date as the input and use zfill() method to return the string in a standard date format (in DD-MM-YYYY).

def perfect_date(day, month, year):
  day = day.zfill(2)
  month = month.zfill(2)
  year = year.zfill(4)
  date = day + '/' + month + '/' + year
  print('The perfect date (DD-MM-YYYY) is: " + date)

date = '2'
month = '6'
year = '2022'
perfect_date(day, month, year)

# Output: The perfect date (DD-MM-YYYY) is: 02/06/2022
