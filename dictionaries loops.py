user_0 = {'name': 'dorothy', 'age': 32, 'occupation': 'doctor'}

for key, value in user_0.items():
    print(key, '---->', value)

print('\nKeys for the dictionary\n')
for key in user_0:
    print(f'---{key}')

print('\nvalue for the dictionary\n')

for value in user_0.values():
    print(f'----{value}')
