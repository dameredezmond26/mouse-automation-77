"""Custom exceptions for the mouse-automation-77 autoclicker.

Performance optimized using __slots__ to reduce object size
in high speed clicking scenarios.
"""

class MouseAutomationError(Exception):
    """Base exception class for mouse automation errors."""
    __slots__ = ('message', 'details')

    def __init__(self, message, details=None):
        """Initialize the error with message and optional details."""
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self):
        """Return formatted error string."""
        if self.details:
            return f"{self.message}: {self.details}"
        return self.message

    def get_info(self):
        """Get error information as dict for logging purposes."""
        return {
            "type": type(self).__name__,
            "message": self.message,
            "details": self.details
        }


class InvalidCoordinatesError(MouseAutomationError):
    """Raised when mouse coordinates are out of valid range."""
    __slots__ = ()


class ClickFailedError(MouseAutomationError):
    """Raised when an automated click action cannot be performed."""
    __slots__ = ()


class AutomationTimeoutError(MouseAutomationError):
    """Raised when a wait or action exceeds the allowed time."""
    __slots__ = ()


class MouseAccessError(MouseAutomationError):
    """Raised when the system denies mouse control access."""
    __slots__ = ()


class InvalidActionError(MouseAutomationError):
    """Raised for unsupported or invalid automation actions."""
    __slots__ = ()


class ResourceError(MouseAutomationError):
    """Raised when required system resources are unavailable."""
    __slots__ = ()


class PerformanceError(MouseAutomationError):
    """Raised when performance metrics indicate issues."""
    __slots__ = ()