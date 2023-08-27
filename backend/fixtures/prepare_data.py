import json


with open('./backend/fixtures/ingredients.json', 'r',
          encoding='utf-8') as input_file:
    ingredients_data = json.load(input_file)

ingredients_to_load = []

for index, ingredient_data in enumerate(ingredients_data, start=1):
    ingredient_to_load = {
        "model": "recipes.ingredient",
        "pk": index,
        "fields": {
            "name": ingredient_data["name"],
            "measurement_unit": ingredient_data["measurement_unit"]
        }
    }
    ingredients_to_load.append(ingredient_to_load)

with open('./backend/fixtures/ingredients_to_load.json', 'w',
          encoding='utf-8') as output_file:
    json.dump(ingredients_to_load, output_file, indent=4, ensure_ascii=False)
