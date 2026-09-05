import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "click_interval": 0.1,  # in seconds
    "button": "left",       # left, right, middle
    "hotkey": "f8",         # toggle activation
    "double_click": False,
    "max_clicks": 0,        # 0 for infinite
}

class ConfigLoader:
    """Loads and manages configuration for the autoclicker application."""
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self.load()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from JSON file, merging with default options."""
        config = DEFAULT_CONFIG.copy()
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        for key, value in user_config.items():
                            if key in config:
                                config[key] = value
            except (json.JSONDecodeError, IOError):
                # Use defaults silently if file is corrupted or unreadable
                pass
        return config

    def save(self) -> bool:
        """Persists the current configuration state back to the disk."""
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except IOError:
            return False

    def get(self, key: str) -> Any:
        """Safely retrieves a configuration key, utilizing defaults as a fallback."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))
