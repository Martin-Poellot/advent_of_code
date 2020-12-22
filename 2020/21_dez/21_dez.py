data = []
import time
with open("21_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.strip('\n'))

ingredients = []
allergens = []
for line in data:
    stuff, allers = line.split(" (")
    ingredients.append(stuff.split(" "))
    allers = allers[:-1].split('contains ')[1]
    allergens.append(allers.split(", "))

# puzzle 1
start_1 = time.time()
ingredients_dict = {}
not_allergens = set()
ingredients_list = []
for i, a in zip(ingredients, allergens):
    ingredients_list += i
    set_i = set(i)
    not_allergens = not_allergens.union(set_i)

    for allergen in a:
        if allergen not in ingredients_dict.keys():
            ingredients_dict[allergen] = set_i
        else:
            ingredients_dict[allergen] = ingredients_dict[allergen].intersection(set_i)

allergic_stuff = set(k for value in ingredients_dict.values() for k in value)
not_allergens = not_allergens.difference(allergic_stuff)
not_allergens_count = sum([i in not_allergens for i in ingredients_list])
elapsed1 = time.time() - start_1
print(f'Puzzle 1: {not_allergens_count}')
print(f'Elapsed Time: {elapsed1:.6f}s')

# puzzle 2:
start_2 = time.time()
while any([len(ingrid) > 1 for ingrid in ingredients_dict.values()]):
    for allerg, ingred in ingredients_dict.items():
        if len(ingred) == 1:
            alg = list(ingred)[0]
            for a2, i2 in ingredients_dict.items():
                if a2 == allerg:
                    continue
                if len(i2) > 1:
                    if alg in i2:
                        ingredients_dict[a2].remove(alg)

dangerous_list = list(ingredients_dict.keys())
dangerous_list.sort()
print(f"My canonical dangerous ingredient list: {','.join([list(ingredients_dict[dangerous])[0] for dangerous in dangerous_list])}")
elapsed2 = time.time() - start_2
print(f'Elapsed Time: {elapsed2:.6f}s')
