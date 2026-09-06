import platform

# Application metadata
APP_NAME = "mouse-automation-77"
VERSION = "1.0.0"

# Mouse button mappings
LEFT_BUTTON = "left"
RIGHT_BUTTON = "right"
MIDDLE_BUTTON = "middle"

# Timing constraints
MIN_CLICK_INTERVAL = 0.01
DEFAULT_INTERVAL = 0.1

# Operating system detection
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"

# Global keyboard hotkeys
START_HOTKEY = "f6"
STOP_HOTKEY = "f7"
EXIT_HOTKEY = "esc"

# Configuration file defaults
CONFIG_FILE = "settings.json"
LOG_FILE = "automation.log"

# UI constraints
DEFAULT_WINDOW_SIZE = "400x300"
THEME_COLOR = "#2c3e50"