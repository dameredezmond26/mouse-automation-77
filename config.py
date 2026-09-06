import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 100,
    "hotkey": "f8"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from json file with defaults fallback.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """
    Saves current configuration to local json file.
    """
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)