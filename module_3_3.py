def print_params( a, b, c):
   print(a, b, c)

list = [1,'строка',True]

print_params(*list)
print_params(a = 1, b = 25, c = [1,2,3])

values_list = ['hello', 27, True]
values_dict = {'a': 2, 'b': 'World', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 =  [54.32, 'Строка' ]
print_params(*values_list_2, 42)