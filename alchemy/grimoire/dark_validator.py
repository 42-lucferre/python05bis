from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_input_list = ingredients.replace(",", "").split(" ")
    for ingredient in ingredients_input_list:
        if ingredient.lower() in (dark_spell_allowed_ingredients()):
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
