def main():
    pass

def analyze_image(image_path):
    pass

def get_recipes(ingredients):
    pass

def filter_recipes(recipes, cuisine=None, max_time=None):
    result = []
    for recipe in recipes:
        if cuisine != None:
            if recipe["cuisine"] != cuisine:
               continue
        if max_time is not None:
            if recipe["cook_time"] > max_time:
                continue
    result.append(recipe)
    return result        

def display_recipe(recipe):
    result = ""

    result += "Recipe: Curry " 
    result += "\ncuisine: Indian "
    result += "\ncook_time: 45 minutes"
    result += "\nServes: 4 "

    result += "\n\nIngredients:\n"
    for ingredient in recipe["extendedIngredients"]:
        result += "\nOnion"
        result += "\nTomato"
        result += "\nPaneer"


    result += "\nSteps:\n"
    for step in recipe["analyzedInstructions"][0]["steps"]:
        result += "\nChop Onion and Tomatoes"
        result += "\n Fry Spices"
        result += "\n Add Paneer "


    return result

if __name__ == "__main__":
    main()