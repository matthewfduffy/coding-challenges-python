"""
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
"""
# Option 1
def smash(words):
    new_string = ""
    for word in words:
        new_string = new_string + " " + word
    return new_string.strip()

test_a = ['hello', 'world', 'this', 'is', 'great']
test_b = ["", 'hello', 'world', 'this', 'is', 'great']

print(smash(test_a))
print(smash(test_b))

# Option 2
def smash(words):
    return " ".join(words)