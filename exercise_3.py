#takes input string and returns a dict with keys of each letter and values of count of each letter with spaces removed
def letter_count(input_string):
    return{letter:input_string.count(letter) for letter in (input_string.replace(" ", ""))}
print(letter_count(input('Please enter a string: ')))