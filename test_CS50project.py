
from CS50project import filter_recipes
def test_filter_recipes():
    recipes = [
        {"name": "Pasta", "cuisine": "Italian", "cook_time": 20},
        {"name": "Curry", "cuisine": "Indian", "cook_time": 45}

    ]
    result = filter_recipes(recipes,cuisine = "Indian")
    assert len(result) == 1
    assert result[0]["name"] == "Curry"

from CS50project import display_recipe
def test_display_recipe():
      recipe = {
          "title": "Curry",
          "cuisines": ["Indian"],
          "cook_time": "45 minutes",
          "servings": 4,
          "extendedIngredients": [
              {"name": "Onion"}
        ],
        "analyzedInstructions": [
            {
                "steps": [
                    {"number": 1, "step": "Chop Onion and Tomatoes"}
                ]
            }
        ]
    }

       


    