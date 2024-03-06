names = ['Anna', 'Oskars', 'Dženifera']
number = ['12345678', '23452347', '87410859']
for i in range(3):
    print(f"{names[i]}: {number[i]}")


for i in range(len(names)):
    print(f" {names[i]}: {number[i]}")




    names = ['Anna', 'Oskars', 'Dženifera']
number = ['12345678', '23452347', '87410859']

new_name = input('uzraksti vardu: ')
new_number = input('uzrakstinumuru: ')


number.append(new_number)
names.append(new_name)

for i in range(len(names)):
    print(f" {names[i]}: {number[i]}")



name_to_delete = input('name to delete:  ')

index_to_remove = names.index(name_to_delete)

names.pop(index_to_remove)
number.pop(index_to_remove)