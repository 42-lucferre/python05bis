#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    from alchemy.transmutation import recipes

    print(f"Testing lead to gold: {recipes.lead_to_gold()}")
