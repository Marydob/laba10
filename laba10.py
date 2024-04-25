import json
with open('products.json', encoding='utf-8') as f:
    data = json.load(f)
for product in data['products']:
    print("Название:", product['name'])
    print("Цена:", product['price'])
    print("Вес:", product['weight'])

    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
import json
new = {
    "name": input("Введите название продукта: "),
    "price": int(input("Введите цену продукта: ")),
    "weight": int(input("Введите вес продукта: ")),
    "available": input("Продукт в наличии?: ")=="да"
}
with open('products.json', 'r', encoding='utf-8') as f:
    products_data = json.load(f)
products_data["products"].append(new)
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products_data, f, ensure_ascii=False, indent=4)
with open('products.json', encoding='utf-8') as f:
    data = json.load(f)
for product in data["products"]:
    print("Название:", product["name"])
    print("Цена:", product["price"])
    print("Вес:", product["weight"])
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")

    print()

with open("en-ru.txt", "r") as file:
    line = file.readlines()
dict_ru_en = {}
for word in line:
    part = word.strip().split(" - ")
    if len(part) == 2:
        ru = part[1]
        en = part[0]
        if ru in dict_ru_en:
            dict_ru_en[ru].append(en)
        else:
            dict_ru_en[ru] = [en]
sort = dict(sorted(dict_ru_en.items()))
with open("ru-en.txt", "w") as file:
    for ru, en in sort.items():
        file.write(ru+" - "+", ".join(en)+"\n")


