"""Custom exception hierarchy for the mouse-automation-77 autoclicker system."""


class AutoclickerError(Exception):
    """Base exception class for all mouse automation errors."""

    def __init__(self, message: str = "An unexpected automation error occurred."):
        self.message = message
        super().__init__(self.message)


class ConfigurationError(AutoclickerError):
    """Raised when application configuration or hotkey settings are invalid."""

    pass


class ClickIntervalError(AutoclickerError):
    """Raised when an invalid click delay or interval value is provided."""

    def __init__(self, interval: float):
        self.interval = interval
        super().__init__(f"Invalid click interval specified: {interval}s (must be > 0).")


class CoordinateOutOfBoundsError(AutoclickerError):
    """Raised when target click coordinates fall outside display bounds."""

    def __init__(self, x: int, y: int, screen_width: int, screen_height: int):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        msg = f"Target ({x}, {y}) out of screen bounds ({screen_width}x{screen_height})."
        super().__init__(msg)


class AutomationStateError(AutoclickerError):
    """Raised when an operation is invalid for current state (e.g. double start)."""

    pass
