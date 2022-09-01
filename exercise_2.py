my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
def combine_dict(dict_1, dict_2):
    return {tup[0]:(tup[1]+dict_2.get(tup[0])) for tup in dict_1.items() if tup[0] in dict_2}
print(combine_dict(my_dict_1, my_dict_2))