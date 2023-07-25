# ws_6_2.py

# 아래 함수를 수정하시오.
def get_value_from_dict(dict1,n_name):
    result = dict1.get(n_name)
    return result

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice
