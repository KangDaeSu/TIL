# ws_6_5.py

# 아래 함수를 수정하시오.
def difference_sets(set1, set2):
    result = set1.difference(set2)
    return result

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
