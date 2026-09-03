import sys
from typing import Final

# Performance thresholds for input injection
# Lower intervals increase CPU load significantly
MIN_CLICK_INTERVAL: Final[float] = 0.001
DEFAULT_CLICK_INTERVAL: Final[float] = 0.01

# Event buffering constants
# Higher batch size reduces overhead in syscalls
EVENT_BATCH_SIZE: Final[int] = 128
MAX_QUEUE_LENGTH: Final[int] = 1024

# System specific optimization settings
IS_WINDOWS: Final[bool] = sys.platform == 'win32'
IS_LINUX: Final[bool] = sys.platform.startswith('linux')

# Threading priority flags
# High priority helps maintain precision at low intervals
THREAD_PRIORITY_HIGH: Final[int] = 1
THREAD_PRIORITY_NORMAL: Final[int] = 0

# Input emulation event codes
MOUSE_EVENT_LEFT_DOWN: Final[int] = 0x0002
MOUSE_EVENT_LEFT_UP: Final[int] = 0x0004
MOUSE_EVENT_RIGHT_DOWN: Final[int] = 0x0008
MOUSE_EVENT_RIGHT_UP: Final[int] = 0x0010

# Precision timing settings for internal loops
PRECISION_SLEEP_THRESHOLD: Final[float] = 0.005