"""Custom exceptions for mouse automation in autoclicker."""

class MouseAutomationError(Exception):
    """Base exception for mouse automation errors."""
    def __init__(self, message="An error occurred during mouse automation"):
        super().__init__(message)
        self.message = message

class CoordinateError(MouseAutomationError):
    """Raised for invalid mouse coordinates."""
    def __init__(self, x, y, message=None):
        if message is None:
            message = f"Invalid coordinates provided: ({x}, {y})"
        super().__init__(message)
        self.x = x
        self.y = y

class ClickError(MouseAutomationError):
    """Raised when a mouse click fails."""
    def __init__(self, button="left", message=None):
        if message is None:
            message = f"Failed to click with {button} button"
        super().__init__(message)
        self.button = button

class TimingError(MouseAutomationError):
    """Raised for invalid or failed timing in operations."""
    def __init__(self, delay, message=None):
        if message is None:
            message = f"Timing error with delay of {delay} seconds"
        super().__init__(message)
        self.delay = delay

class AutomationStoppedError(MouseAutomationError):
    """Raised when the automation is stopped unexpectedly."""
    def __init__(self, message="Automation was stopped"):
        super().__init__(message)


def raise_for_operation(operation, **kwargs):
    """Helper to raise appropriate exception for common operations."""
    if operation == "move_mouse":
        x = kwargs.get("x", 0)
        y = kwargs.get("y", 0)
        raise CoordinateError(x, y)
    elif operation == "click":
        button = kwargs.get("button", "left")
        raise ClickError(button)
    elif operation == "wait":
        delay = kwargs.get("delay", 0)
        raise TimingError(delay)
    else:
        raise MouseAutomationError(f"Unknown operation: {operation}")

def handle_common_error(error):
    """Helper function to categorize and return info on common errors."""
    if isinstance(error, CoordinateError):
        return {"type": "coordinate", "details": str(error)}
    elif isinstance(error, ClickError):
        return {"type": "click", "details": str(error)}
    elif isinstance(error, TimingError):
        return {"type": "timing", "details": str(error)}
    elif isinstance(error, AutomationStoppedError):
        return {"type": "stopped", "details": str(error)}
    else:
        return {"type": "unknown", "details": str(error)}