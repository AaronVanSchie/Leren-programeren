from fruitmand import fruitmand

total_weight = 0
fruitmand.append({'name': 'watermeloen', 'weight': 2000, 'color': 'green', 'round': True})

for fruit in fruitmand:
    weight = fruit['weight']
    total_weight += weight
print(total_weight)