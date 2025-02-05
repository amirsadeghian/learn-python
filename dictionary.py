cabinet = dict()
cabinet['beta']= 45
cabinet['alpha']= 21
cabinet['omega'] = 98
print(cabinet)

for key,val in cabinet.items():
    print(key,'=',val)

print('Keys:')
print(cabinet.keys())

print('Values:')
print(cabinet.values())

print('Tuples:')
print(cabinet.items())

print(cabinet.get('alpha','Not found'))


for item in cabinet:
    print(cabinet[item])


dict2 = {}
dict2['name'] = 'Amir'
print(dict2)

dict3 = {'age': 1}
print(dict3)