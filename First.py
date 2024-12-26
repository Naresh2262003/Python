# Original dictionary
original_dict = {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}

# Transforming into a list of dictionaries
list_of_dicts = [{'Boys': b, 'Girls': g} for b, g in zip(original_dict['Boys'], original_dict['Girls'])]

# Display the result
print(list_of_dicts)