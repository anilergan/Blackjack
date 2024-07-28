liste = ['seat1', 'seat2', 'seat3', 'seat1']

dict1 = {key: value for key, value in zip([item for item in liste if item != 'seat1'], [10]*len(liste))}
print(dict1)

# print(liste.count('seat1'))

# dict1 = {
#     'seat1': None, 
#     'seat2': None,
# }

# dict2 = {
#     'hey': 'selam'
# }

# if None not in dict
# u = dict1.values()).count(None)

# print(u)

# import ss

# print(ss.ss_groupbox_bet_active)


# set1 = set()

# print(type(set1))