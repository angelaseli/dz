def calculate_structure_sum(item):
    add = 0
    if isinstance(item, (int, float)):
        add += item
    elif isinstance(item, str):
        add += len(item)
    elif isinstance(item, (list, set, tuple)):
        for elem in item:
            add += calculate_structure_sum(elem)
    elif isinstance(item, dict):
        for key, value in item.items():
            add += calculate_structure_sum(key)
            add += calculate_structure_sum(value)
    return add


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)