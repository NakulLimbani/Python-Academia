
#*i) Extract a four-digit number followed by space followed by a three-digit number:*
import re

s1 = '123456 7890 123'
pattern = r'\b\d{4} \d{3}\b'
result = re.findall(pattern, s1)
print(result)


#*ii) Remove all whitespaces in the given string:*

import re

s2 = 'hai 123 \wishes 345 to all \n'
pattern = r'\s+'
replacement = ''
result = re.sub(pattern, replacement, s2)
print(result)

"""
#*iii) Split the given string only at the first occurrence of a digit:*
"""
import re

s3 = 'Hundred:100 One:1 Twenty:20'
pattern = r'\d'
result = re.split(pattern, s3,1)
print(result)


#*iv) Extract the numbers from the given string:*

import re

s4 = 'Hello 123 Hai 456 hey 789'
pattern = r'\d+'
result = re.findall(pattern, s4)
print(result)
