shopping_list = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

count = 0
for key, values in shopping_list.items():
    new_values = [v.capitalize() for v in values]
    print(f"Idę do {key.capitalize()} i kupuję tam: {new_values}")
    count += len(values)
print(f"W sumie kupuję {count} produktów.")