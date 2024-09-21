def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('cube',2)
print_params([72,14], True, 'Vision')
print_params(b = 26)
print_params(c = [1,2,3])

values_list = [1, 'word', True]
print(values_list)
values_dict = {'a':1, 'b':2, 'c':3}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 'list']
print_params(*values_list_2,42)