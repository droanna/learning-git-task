shopping_list = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

for key, values in shopping_list.items():
    print(f"Idę do {key} i kupuję tam: {values}")