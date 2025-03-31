str_pat = re.compile(r'\"(.*?)\"')      # matches text encolosed inside a pair of qoutes
datepat = re.compile(r'\d+/\d+/\d+')    # matches `DD/MM/YYY`

# Check to see if a sting starts with different patterns
# 2.2 Matching Text at the Start or End of a String pp 38-40 Python Cookbook
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(tuple(choices))

#OR
choices = tuple(['http:', 'ftp:'])
url = 'http://www.python.org'
print(url.startswith(choices))
#---------------------------------------------------------

# 2.3 Matching Strings Using Shell Wildcard Patterns
from fnmatch import fnmatch, fnmatchcase

fnmatch('foo.txt', '*.txt')     # True
fnmatch('foo.txt', '?oo.txt')   # True
fnmatch('Dat45.csv', 'Dat[0-9]*')   # Tru

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]
    # ['Dat1.csv', 'Dat2.csv']
#---------------------------------------------------------

# Matching Dates
text1 = "11/27/2021"
text2 = 'Nov. 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):
    print("Yes")
else:
    print("No")

# when performing several matches using the same pattern, precompile the regex into a pattern object first
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    pass
if datepat.match(text2):
    pass

# match() always tries to find the match at the start of a string
# to search for all occurrences of a pattern use findall()
text = 'Today is 11/27/2021. Pycon starts 3/13/2022'
datepat.findall(text)   # ['11/27/2021', '3/13/2022']
# ---------------------------------------------------------------------
#Searching Case-Sensitive Text
text = 'UPPER PYTHON, lower python, Mixed Python'

import re
re.findall('python, text, flags=re.IGNORECASE')
# ['PYTHON', 'python, 'Python']

# Replacing Case-Sensitive Text Matches
re.sub('python', 'snake', text, flags=re.IGNORECASE)
#'UPPER snake, lower snake, Mixed snake'