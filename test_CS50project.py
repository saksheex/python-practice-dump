
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
          "cook_time": 45,
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
    result = display_recipe(recipe)
    assert "Curry" in result
    assert "45" in result
    assert "Onion" in result
    assert "Chop Onion and Tomatoes" in result


from CS50project import get_recipes
from unittest.mock import patch, MagicMock
def test_get_recipes():
    fake_response = [
    {"title": "Paneer Curry", "cuisines": ["Indian"],"cook_time": 40}
    ]
    mock_get = MagicMock()
    mock_get.json.return_value = fake_response

    with patch("requests.get", return_value=mock_get):
     result = get_recipes(["Onion", "Tomato", "Paneer"])
     assert type(result) == list
     assert len(result) == 1


    