#!/usr/bin/env python3

import sys
import os
import site


if sys.prefix == sys.base_prefix:
    print("\nLABORATORY STAUTS: You are working in the open")

    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")

    print("\nTo seal the laboratory, run:")
    print("""python3 -m venv lab_env
source lab_env/bin/activate # On Unix
lab_env\\Scripts\\activate # On Windows""")

    print("\nThen run this program again.")

else:
    print("\nLABORATORY STAUTS: The laboratory is sealed")

    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")

    print("\nSUCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")

    print("\nReagent installation path:")
    print(f"{site.getsitepackages()[0]}")
