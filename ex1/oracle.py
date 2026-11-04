#!/usr/bin/env python3

import os
import sys


CONFIG_VARS = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
               "LOG_LEVEL", "ZION_ENDPOINT"]


def no_hardcoded_secrets() -> bool:
    try:
        with open(os.path.abspath(__file__)) as f:
            lines = f.readlines()
    except OSError:
        return True
    for line in lines:
        s = line.strip()
        if s.startswith("#") or "=" not in s:
            continue
        for key in CONFIG_VARS:
            if s.startswith(key) and s[len(key):].lstrip().startswith("="):
                value = s.split("=", 1)[1].strip()
                if value.startswith('"') or value.startswith("'"):
                    return False
    return True


def overrides_available() -> bool:
    original = os.environ.get("MATRIX_MODE")
    os.environ["MATRIX_MODE"] = "__test__"
    try:
        call_dotenv()
        if os.environ.get("MATRIX_MODE") == "__test__":
            return True
        else:
            return False
    finally:
        if original is None:
            os.environ.pop("MATRIX_MODE", None)
        else:
            os.environ["MATRIX_MODE"] = original


def env_ignored() -> bool:
    env_variations = [".env", "*.env"]
    try:
        with open(os.path.join(os.path.dirname(os.path.
                  abspath(__file__)), ".gitignore")) as f:
            ignored = [line.strip() for line in f]
            for variation in env_variations:
                if variation in ignored:
                    return True
            return False
    except Exception:
        return False


def call_dotenv() -> None:
    dotenv.load_dotenv(dotenv_path=os.path.
                       join(os.path.dirname(os.
                            path.abspath(__file__)), ".env"), override=False)


if __name__ == "__main__":
    try:
        import dotenv  # type: ignore
    except ImportError as e:
        print(f"[Error] {e} ")
        print("Use 'pip install -r ex1/requirements'")
        sys.exit(1)

    print("\nORACLE STATUS: Consulting the configuration...")

    call_dotenv()

    config = {}
    missing = []
    for key in CONFIG_VARS:
        value = os.getenv(key)
        if value is None or value.strip() == "":
            missing.append(key)
        else:
            config[key] = value.strip()

    mode = config.get("MATRIX_MODE", "production")

    print("\nConfiguration loaded:")

    if mode == "production":
        config["DATABASE_URL"] = "Connected (URL hidden)"
        config["API_KEY"] = "Authenticated (Hidden)"
        config["LOG_LEVEL"] = "Hidden"
        config["ZION_ENDPOINT"] = "Online (URL hidden)"

    if "MATRIX_MODE" not in missing:
        print(f"Mode: {mode}")
    else:
        print("[WARNING] Mode not configured, set to default (production)")

    if "DATABASE_URL" not in missing:
        print(f"Database: {config['DATABASE_URL']}")
    else:
        print("[WARNING] Database not configured]")

    if "API_KEY" not in missing:
        print(f"API Access: {config['API_KEY']}")
    else:
        print("[WARNING] API key not configured]")

    if "LOG_LEVEL" not in missing:
        print(f"Log Level: {config['LOG_LEVEL']}")
    else:
        print("[WARNING] Log Level not configured]")

    if "ZION_ENDPOINT" not in missing:
        print(f"Remote Network: {config['ZION_ENDPOINT']}")
    else:
        print("[WARNING] Remote Network not configured")

    print("\nConfiguration security check:")

    if no_hardcoded_secrets():
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Hardcoded secrets detected")

    if env_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file not ignored by git")

    if overrides_available():
        print("[OK] Production overrides available")
    else:
        print("[WARNING] Overrides not available")

    print("The Oracle sees all configurations.")
