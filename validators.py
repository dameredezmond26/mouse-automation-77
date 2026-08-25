"""Validators for mouse automation parameters."""

from typing import Tuple, Optional

def validate_screen_coordinates(x: int, y: int, screen_width: int = 1920, screen_height: int = 1080) -> bool:
    """Validate coordinates within screen bounds.

    Args:
        x: x position, y: y position, screen_width: max x, screen_height: max y
    Returns:
        True if valid.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        return False
    return 0 <= x < screen_width and 0 <= y < screen_height

def validate_click_interval(interval: float) -> bool:
    """Validate interval >0 and <=1 hour.

    Args:
        interval: seconds between clicks
    Returns:
        True if valid.
    """
    if not isinstance(interval, (int, float)):
        return False
    return 0 < interval <= 3600

def validate_click_count(count: int) -> bool:
    """Validate positive click count.

    Args:
        count: number of clicks
    Returns:
        True if valid.
    """
    if not isinstance(count, int):
        return False
    return count > 0

def validate_button(button: str) -> bool:
    """Validate supported mouse button.

    Args:
        button: left, right or middle
    Returns:
        True if valid.
    """
    if not isinstance(button, str):
        return False
    return button.lower() in {"left", "right", "middle"}

def get_validated_params(x: int, y: int, interval: float, count: int, button: str) -> Optional[Tuple[int, int, float, int, str]]:
    """Return params if all valid else None.

    Args:
        x, y: coords, interval: time, count: clicks, button: type
    Returns:
        tuple of validated or None
    """
    if (validate_screen_coordinates(x, y) and validate_click_interval(interval) and
            validate_click_count(count) and validate_button(button)):
        return (x, y, interval, count, button.lower())
    return None