def valid_input():
    inputs = []
    while(len(inputs)<5):
        try:
            inputs.append(int(input(f'Enter int #{len(inputs)+1}: ')))
        #if not (inputs[-1].isdigit()):
        except:
            print('Invalid input. Please enter an int.')
    return(sum(list(map(int, inputs))))
print(valid_input())
