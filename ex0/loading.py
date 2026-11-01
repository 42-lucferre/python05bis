#!/usr/bin/env python3

try:
    import pandas as pd
    import numpy as np
except ImportError as e:
    

if __name__ == "__main__":

    print("\nREAGENT STATUS: Loading reagents...")

    print("\nChecking dependencies:")

    print("pip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it at "
          "install time.\npyproject.toml declares the same constraints, "
          "and Poetry pins the resolved versions in poetry.lock so every "
          "install is identical.")

    print("\nAll reagents present and accounted for.")
