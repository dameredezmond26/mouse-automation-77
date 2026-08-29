import json
import os

class ConfigLoader:
    """Loads configuration with defaults for the autoclicker."""

    DEFAULTS = {
        "click_interval": 0.5,  # Time between clicks in seconds
        "click_count": 0,  # Total clicks, 0 for continuous
        "mouse_button": "left",
        "randomize": True,
        "random_min": 0.3,
        "random_max": 0.7,
        "hotkey": "f8",
        "target_position": None,
    }

    def __init__(self, filename="config.json"):
        self.filename = filename
        self.config = self.DEFAULTS.copy()
        self.load_config()

    def load_config(self):
        """Load from file if present, merge with defaults."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    loaded = json.load(file)
                    for key in self.DEFAULTS:
                        if key in loaded:
                            self.config[key] = loaded[key]
            except Exception:
                # On any error, use defaults
                self.config = self.DEFAULTS.copy()

    def save_config(self):
        """Write the configuration to disk."""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.config, file, indent=4)
        except Exception:
            pass

    def get(self, key, default=None):
        """Retrieve a configuration value."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Update a value and save to file."""
        if key in self.DEFAULTS:
            self.config[key] = value
            self.save_config()

    def get_all(self):
        """Return dictionary of all settings."""
        return self.config.copy()

    def apply_defaults(self):
        """Ensure all default keys are present."""
        for key, value in self.DEFAULTS.items():
            if key not in self.config:
                self.config[key] = value
