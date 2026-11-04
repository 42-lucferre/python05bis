def validate_ingredients(ingredients: str) -> str:
    from . import light_spellbook

    ingredients_input_list = ingredients.replace(",", "").split(" ")
    for ingredient in ingredients_input_list:
        if ingredient.lower() in (light_spellbook.
                                  light_spell_allowed_ingredients()):
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
