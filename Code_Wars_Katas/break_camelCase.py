"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def break_camelCase(s):
	return_word = " "
    if s.islower():
    	return s
    else:
    	for letter in s:
    		if letter.islower():
    			return_word += letter
    		else:
    			return_word += "" + letter.lower()
    
    if return_word != ""
    return return_word
    	








# Test/s
a = "camelCase"
b = "lowercase"
c = ""

print(break_camelCase(a))