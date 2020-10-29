colors='red-orange-yellow-green-blue'
items=[i for i in colors.split('-')]
items.sort()
print('-'.join(items))