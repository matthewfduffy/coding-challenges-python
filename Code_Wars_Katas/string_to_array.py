"""
Write a function to split a string and convert it into an array of words.
Examples (Input ==> Output):

"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

"""
def string_to_array(s):
    return s.split(" ")






test_a = "Robin Singh"
test_b = "I love arrays they are my favorite"

print(string_to_array(test_a))
print(string_to_array(test_b))