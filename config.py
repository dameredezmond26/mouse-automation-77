import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_count": 0
}

def load_config(filepath: str = "config.json") -> dict:
    """Loads configuration from JSON file with fallback to defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: dict, filepath: str = "config.json") -> None:
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")