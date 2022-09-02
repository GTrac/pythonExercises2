#takes in 2 dictionaries and returns dict of only shared keys with corresponding values from both dicts summed
def combine_dict(dict_1, dict_2):
    return {key1:(dict_1.get(key1)+dict_2.get(key1)) for key1 in dict_1.keys() if key1 in dict_2}
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
print(combine_dict(my_dict_1, my_dict_2))