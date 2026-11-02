#!/usr/bin/env python3

import importlib

if __name__ == "__main__":

    print("\nREAGENT STATUS: Loading reagents...")

    print("\nChecking dependencies:")

    deps = ["pandas", "numpy"]
    missing_deps = 0

    for dep in deps:
        try:
            module = importlib.import_module(dep)
            if module.__name__ == "pandas":
                description = "Data manipulation"
            if module.__name__ == "numpy":
                description = "Numerical computation"
            print(f"[OK] {dep} ({module.__version__}) - {description} "
                  "ready")
        except ModuleNotFoundError:
            missing_deps = 1
            print(f"[Error] {dep} not installed.")

    if missing_deps:
        print("\nUse 'pip install -r ex0/requirements.txt' or 'poetry -C ex0/ "
              "install' before running the program again.")
    else:
        print("\npip vs Poetry:")
        print("""\
    requirements.txt declares what to install; pip resolves it at install time.
    pyproject.toml declares the same constraints, and Poetry pins the resolved
    versions in poetry.lock so every install is identical.""")

        print("\nAll reagents present and accounted for.")
