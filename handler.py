import time
from typing import Optional, Tuple
import pyautogui

def get_current_position() -> Tuple[int, int]:
    """Retrieve the current mouse cursor position.

    Returns:
        A tuple containing the x and y coordinates of the mouse.
    """
    return pyautogui.position()

def perform_single_click(
    x: Optional[int] = None,
    y: Optional[int] = None,
    button: str = "left"
) -> None:
    """Perform a single mouse click at the specified or current position.

    If x or y is None, the current mouse position is used.

    Args:
        x: Horizontal coordinate for the click.
        y: Vertical coordinate for the click.
        button: The mouse button to use for clicking.
    """
    if x is None or y is None:
        pos = get_current_position()
        # Use current if coordinates not provided
        x = pos[0] if x is None else x
        y = pos[1] if y is None else y
    pyautogui.click(x=x, y=y, button=button)

def run_autoclicker(
    total_clicks: int,
    click_interval: float = 0.1,
    initial_delay: float = 2.0
) -> None:
    """Run the autoclicker for a specified number of clicks.

    Clicks are performed at the current mouse position with given interval.

    Args:
        total_clicks: The total number of clicks to execute.
        click_interval: Delay between consecutive clicks in seconds.
        initial_delay: Time to wait before starting the clicking sequence.
    """
    time.sleep(initial_delay)
    # execute clicks in loop
    for i in range(total_clicks):
        pyautogui.click()
        time.sleep(click_interval)
    print(f"Autoclicker finished after {total_clicks} clicks.")

def click_at_position(
    position: Tuple[int, int],
    num_clicks: int = 1,
    interval: float = 0.05
) -> bool:
    """Click at a specific screen position multiple times.

    Args:
        position: Tuple of (x, y) screen coordinates.
        num_clicks: How many times to click.
        interval: Seconds between each click if multiple.
    Returns:
        True if all clicks were successful.
    """
    x, y = position
    try:
        pyautogui.click(x=x, y=y, clicks=num_clicks, interval=interval)
        return True
    except Exception:
        return False