#takes in input list and returns list of only unique elements
def unique_list(input_list):
    return [y for y in input_list if input_list.count(y)<2]
test_list = [1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9]
print(unique_list(test_list))