# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dict1, name1, name2):
    new_dict = dict1.copy()
    otherdict = {name1: name2}
    new_dict.update(otherdict)
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
