# Example 1: Days of the week

days = 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

[d[:3] for d in days] # returns ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days_abbr = [d[:3] for d in days]
print(days)
print(days_abbr)

[d.upper() for d in days] # returns ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
[d[-1] for d in days] # returns ['y', 'y', 'y', 'y', 'y', 'y', 'y']

days_copy = [ d for d in days ] # make a copy of the list

# OR: use a for loop 

days_abbr = []

for d in days:
  days_abbr.append(d[:3])
print(days_abbr)

# Output: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# IF LAST LINE WAS INDENTED:

days_abbr = []

for d in days:
  days_abbr.append(d[:3])
  print(days_abbr)

# Output: 

'''
['Sun']
['Sun', 'Mon']
['Sun', 'Mon', 'Tue']
['Sun', 'Mon', 'Tue', 'Wed']
['Sun', 'Mon', 'Tue', 'Wed', 'Thu']
['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
'''

[d for d in days if d[0] == 'S'] # returns the days of the weekend: ['Sunday', 'Saturday']

[d[:3] for d in days if d[0] == 'S'] # returns the abbreviations for the days of the weekend: ['Sun', 'Sat']

# Example 2: Age check

ages = [18, 24, 22, 17, 20, 21, 19, 18, 20, 25]  
over21 = [(age > 21) for age in ages] # returns [False, True, True, False, False, False, False, False, False, True]

# Example 3: Names to e-mails

names = ['Marcel Marcellinus', 'Sander Otobong', 'Linda Katashi', 'Vasant Avinash', 'Xochiquetzal Erasyl', 'Xiaolan Li']

print('this-string-has-lots-of-hyphens'.replace('-', ' '))  # returns 'this string has lots of hyphens
print('this-string-has-lots-of-hyphens'.replace('-', ''))   # returns thisstringhaslotsofhyphens

print( 'Marcel Marcellinus'.replace(' ', '.') )  # returns Marcel.Marcellinus         
print( 'Marcel Marcellinus'.replace(' ', '.').lower() )  # returns marcel.marcellinus
print( 'Marcel Marcellinus'.replace(' ', '.').lower() + '@example.com' )  # returns marcel.marcellinus@example.com

prices = [1.5, 2.35, 5.99, 16.49]
sum(prices)

# OR: use a for loop

prices = [1.5, 2.35, 5.99, 16.49]
our_sum = 0 

for price in prices:
  out_sum += price
  
print(out_sum)

# Example 4: Phone numbers - let's say we have to go through lots of phone numbers, some with hyphens, some without, and get them in the same format, without hyphens.

phonenumbers_messy = ['321-456-7890', '7653459876', '901 432-5678', '(654) 1237654', '911-012-6543', '(456) 890-4321']
print(phonenumbers_messy)

phonenumbers_clean = [num.replace('-', '') for num in phonenumbers_messy]
print(phonenumbers_clean) # returns ['3214567890', '7653459876', '901 4325678', '(654) 1237654', '9110126543', '(456) 8904321']
phonenumbers_clean2 = [num.replace('(', '') for num in phonenumbers_clean] # gets rid of left parenthesis 
print(phonenumbers_clean2) # returns ['3214567890', '7653459876', '901 4325678', '654) 1237654', '9110126543', '456) 8904321']
phonenumbers_clean3 = [num.replace(')', '') for num in phonenumbers_clean2] # gets rid of right parenthesis
print(phonenumbers_clean3) # returns ['3214567890', '7653459876', '901 4325678', '654 1237654', '9110126543', '456 8904321']
phonenumbers_clean4 = [num.replace(' ', '') for num in phonenumbers_clean3] # gets rid of spaces
print(phonenumbers_clean4) # returns ['3214567890', '7653459876', '9014325678', '6541237654', '9110126543', '4568904321']

phonenumbers_clean5 = [(num[:3] + '-' + num[3:6] + '-' + num[6:]) for num in phonenumbers_clean4]
print(phonenumbers_clean5) # returns ['321-456-7890', '765-345-9876', '901-432-5678', '654-123-7654', '911-012-6543', '456-890-4321']

# Method 1:

phonenumbers_messy = [ '321-456-7890', '7653459876', '901 432-5678', '(654) 1237654', '911-012-6543', '(456) 890-4321' ]
phonenumbers_clean = []
for num in phonenumbers_messy:
  num = num.replace('-', '') # rewrite num without hyphens, if it has any
  num = num.replace(' ', '') # rewrite num without spaces, if it has any
  num = num.replace('(', '') # rewrite num without parentheses, if it has any
  num = num.replace(')', '')
  num = num[:3] + '-' + num[3:6] + '-' + num[6:] # build num back up
  phonenumbers_clean.append(num) # add num to the new list
print(phonenumbers_clean) # returns ['321-456-7890', '765-345-9876', '901-432-5678', '654-123-7654', '911-012-6543', '456-890-4321']

# Method 2: 
phonenumbers_messy = [ '321-456-7890', '7653459876', '901 432-5678', '(654) 1237654', '911-012-6543', '(456) 890-4321' ]
phonenumbers_clean = []
for num in phonenumbers_messy:
  num1 = num.replace('-', '') # rewrite num without hyphens, if it has any
  num2 = num.replace(' ', '') # rewrite num without spaces, if it has any
  num3 = num.replace('(', '') # rewrite num without parentheses, if it has any
  num4 = num.replace(')', '')
  num5 = num4[:3] + '-' + num4[3:6] + '-' + num4[6:]
  phonenumbers_clean.append(num5)
print(phonenumbers_clean)

# Example 5: From a list of words, return the ones that begin and end with the same letter

word_list = ['bandana', 'hyperboreal', 'blurb', 'defied', 'cankerousness', 'heist', 'polyp', 'bouldering', 'elegiac', 'kayak']
words_caught = [w for w in word_list if w[0] == w[-1]]
print(words_caught) # returns ['blurb', 'defied', 'polyp', 'kayak']

# OR: filter for the opposite criterion

words_missed [w for w in word_list if w[0] != w[-1]]
print(words_missed) # returns ['bandana', 'hyperboreal', 'cankerousness', 'heist', 'bouldering', 'elegiac']

# With both the list of words caught and list of words missed, we should be able to reconstruct the original list:

word_list2 = words_caught + words_missed
word_list2.sort
word_list.sort
word_list == word_list 2 # returns True

# Example 6: From a list of words, return those that are more than 10 characters long

word_list = ['bandana', 'hyperboreal', 'blurb', 'defied', 'cankerousness', 'heist', 'polyp', 'bouldering', 'elegiac', 'kayak']
sat_words = [w for w in word_list if len(w) > 10]
print(sat_words) # returns ['hyperboreal', 'cankerousness']

# Example 7: Filtering a list of first names and a list of last names to determine which first names are sometimes last names

firstnames = [ 'Michel', 'Elsa' , 'Akshay', 'Marianne', 'Patricius', 'Hamid'   ]
surnames   = [ 'Nout'  , 'Reese', 'Akshay', 'Michel'  , 'Matteus'  , 'Velemir' ]

universalnames = []
for n in firstnames:
  if n in surnames:
    universalnames.append(n)
print(universalnames) # returns ['Michael', 'Akshay']

# Example 8: Filtering a list of first names and a list of last names to determine which first names are not last names

firstnames = [ 'Michel', 'Elsa' , 'Akshay', 'Marianne', 'Patricius', 'Hamid'   ]
surnames   = [ 'Nout'  , 'Reese', 'Akshay', 'Michel'  , 'Matteus'  , 'Velemir' ]

firstonlynames = []
for n in firstnames:
  if n not in surnames:
    firstonlynames.append(n)
print(firstonlynames) # returns ['Elsa', 'Marianne', 'Patricius', 'Hamid]

# Example 8: Filtering a list of first names and a list of last names to determine which last names are not first names

firstnames = [ 'Michel', 'Elsa' , 'Akshay', 'Marianne', 'Patricius', 'Hamid'   ]
surnames   = [ 'Nout'  , 'Reese', 'Akshay', 'Michel'  , 'Matteus'  , 'Velemir' ]

lastonlynames = []
for n in surnames:
  if n not in firstnames:
    lastonlynames.append(n)
print(lastonlynames) # returns ['Nout', 'Reese', 'Matteus', 'Velemir']

# Example 9: List out all of the possible combination between list 1 and list 2

modifiers = ["Green", "Oak", "Cherry", "Ever", "North", "Grass", "Stone", "Spring", "Summer", "Fall"]
geography = ["creek", "park", "wood", "brook", "grove", "glen", "ridge", "hurst", "dale", "crest"] 

for modifier in modifiers:
  for feature in geography:
    print(modifier + feature)


# Example 10: Anagram 

word1 = 'itch'
word2 = 'chicklet'

are_anagrams = True # assume all words are anagrams until proven True
if len(word1) == len(word2): 
  word1_list = list(word1)
  word2_list = list(word2)
  for letter in word1_List:
    if letter not in word2_list:
      are_anagrams = False
else:
  are_anagrams = False
print('Is it true that "{}" and "{}" are anagrams? Our code says: {}'.format(word1, word2, are_anagrams))

[name.replace(' ', '.').lower() + '@example.com' for name in names]
