from fruitmand import fruitmand

a = sorted(fruitmand, key=lambda i: i['weight'])
for i in reversed(a):
    print(f'{i["name"]}: {i["weight"]}')