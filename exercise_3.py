def letter_count(input_string):
    return{letter:input_string.count(letter) for letter in (input_string.replace(" ", ""))}
print(letter_count(input('Please enter a string: ')))