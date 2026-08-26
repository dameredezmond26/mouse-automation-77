import json
import os

CONFIG_FILE = "autoclicker_config.json"


def load_autoclicker_config():
    """Load autoclicker configuration from local JSON file."""
    if not os.path.exists(CONFIG_FILE):
        return default_config()
    
    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            return {**default_config(), **data}
    except (json.JSONDecodeError, IOError):
        return default_config()


def save_autoclicker_config(config_data):
    """Save autoclicker configuration to local JSON file."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config_data, f, indent=4)
        return True
    except IOError:
        return False


def default_config():
    """Provide default settings for the autoclicker."""
    return {
        "cps": 10,
        "button": "left",
        "toggle_key": "f6",
        "hold_mode": False,
        "sound_enabled": True
}
