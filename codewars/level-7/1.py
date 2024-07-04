def binary_array_to_number(arr):
  return int("".join(str(i) for i in arr), base=2)

binary_array_to_number([1,1,0,1])