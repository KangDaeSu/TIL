# ws_5_3.py

# 아래 함수를 수정하시오.
# def sort_tuple(original):
#   new_tuple = (list(original))
#   new_tuple.sort()
#   new_tuple = tuple(new_tuple)
#   return new_tuple

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)

# 방법 1.
def sort_tuple(original):
  result = sorted(original)
  return tuple(result)
result = sort_tuple((5, 2, 8, 1, 3))
print(result)
