shake = {'fruits': 'banana mango ', 'milk': 'oatmeal'}

if shake['milk'] == 'oatmeal':
    berry = 'strawberry'
else:
    berry = 'blueberry'

shake['fruits'] = shake['fruits'] + berry

print(f"New fruits are {shake['fruits']}")
