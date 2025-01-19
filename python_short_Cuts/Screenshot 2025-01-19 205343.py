string_One = 'key1key2key3key4'
String_two = 'val1val2val3val4'

# How to get below output?
Result = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'ke4': 'val4'}


# Where do you can get code?
# Here you can get : https://github.com/shivashankars-github/SDET_QA_Analyst/blob/main/README.md


#creating a list of values for dictionary keys from string_one
string_One_as_keys = [string_One[i:i+4] for i in range(0,len(string_One),4)]
# print(string_One_as_keys)
# ['key1', 'key2', 'key3', 'key4']
String_two_as_values = [String_two[i:i+4] for i in range(0,len(String_two),4)]
# print(String_two_as_values)
# ['val1', 'val2', 'val3', 'val4']

"""USING ABOVE TWO LISTS MAKING ONE DICTIONARY"""
dictONe = {k:v for k,v in zip(string_One_as_keys,String_two_as_values)}
# print(dictONe)
# {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'ke4': 'val4'}
dictTwo = {k:String_two_as_values[i] for i,k in enumerate(string_One_as_keys)}
# print(dictTwo)
# {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'ke4': 'val4'}
dictThree = {k:v for i,k in enumerate(string_One_as_keys) for j,v in enumerate(String_two_as_values) if i==j }
# print(dictThree)
# {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'ke4': 'val4'}
assert dictONe==dictTwo==dictThree
print("Yes all are same")