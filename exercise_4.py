#takes in user input until 5 valid int inputs are entered and returns the sum of valid inputs
def valid_input():
    inputs = []
    while(len(inputs)<5):
        try:
            inputs.append(int(input(f'Enter int #{len(inputs)+1}: ')))
        except:
            print('Invalid input. Please enter an int.')
    return(sum(list(map(int, inputs))))
print(valid_input())
