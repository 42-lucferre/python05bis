def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from . import light_validator

    validation = light_validator.validate_ingredients(ingredients)
    if "INVALID" in validation:
        return f"Spell rejected: {spell_name} {validation}"
    elif "VALID" in validation:
        return f"Spell recorded: {spell_name} {validation}"
    else:
        return "light_validator error"
