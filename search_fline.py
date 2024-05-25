import os 

with data(examplefile, 'r') as outfile:
  data = outfile.readlines()

# Searching for a pattern in a file 

for line in data:
  if 'Final Energy' in line:
    energy_line = line 
    print(energy_line)

# Example output: @DF-RHF Final Energy:  -154.09130176573018

words = energy_lines.split() # if you do not specify a delimiter, a space is used by default
energy = words[3]
print(energy)

# Output: ['@DF-RHF', 'Final', 'Energy:', '-154.09130176573018']
# OR: we can use the colon (:) as the delimiter

energy.line.split(':')

# Output: [' @DF-RHF Final Energy', '-154.09130176573018\n']

# Exercise: Use the provided sapt.out file. In this output file, the program calculates the interaction energy for an ethene-ethyne complex. The output reports 
# four interaction energy components: electrostatics, induction, exchange, and dispersion. Parse each of these energies, in kcal/mole, from the output file. 
# Calculate the total interaction energy by adding the four components together. Your code's output should look something like this:

'''
Electrostatics : -2.25850118 kcal/mol
Exchange : 2.27730198 kcal/mol
Induction : -0.5216933 kcal/mol
Dispersion : -0.9446677 kcal/mol
Total Energy : 1.4475602000000003 kcal/mol
'''

important_lines = []
energies = []
with open('sapt.out', 'r') as saptout:
  for line in saptout:
    if 'Electrostatics' in line:
      electro_line = line
      important_lines.append(electro_line)
    if 'Exchange' in line:
      exchange_line = line
      important_lines.append(exchange_line)
    if 'Induction' in line:
      induction_line = line
      important_lines.append(induction_line)
    if 'Dispersion' in line:
      dispersion_line = line
      important_lines.append(dispersion_line)
    print(important_lines)

for line in important_lines: 
  words = line.split()
  energy_type = words[0]
  energy_kcal = float(words[3]
  energies.append(energy_kcal)
  print('{} : {} kcal/mol'.format(energy_type, energy_kcal))

total_energy = sum(energies)
print('Total Energy: {} kcal/mol'.format(total_energy))

# Searching for a particular line number in your file 
# The general syntax is:

for linenum, line in enumerate(list_name):
  do something

# Enumerate with index other than 0: enumerate(list_name) will start with 0 index, so the first line will be labelled as '0'; to change this behaviour, use start variable in enumerate
# e.g. to start with index of '1' you can do: 

for linenum, line in enumerate(data, start=1):
  do something 

# Example block of code that searches a given file for the line that contains 'Center' and reports the line number

for linenum, line in enumerate(date):
  if 'Center' in line:
    print(linenum)
    print(line)

# Example output: we can see that this is line 77 in the file (you start counting from 0!)
