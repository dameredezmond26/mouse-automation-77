import time
import random
from pynput import mouse
from typing import Tuple

def get_random_delay(min_delay: float = 0.05, max_delay: float = 0.5) -> float:
    """Generate a random delay between min and max seconds."""
    return random.uniform(min_delay, max_delay)

def move_to_position(controller: mouse.Controller, x: int, y: int) -> None:
    """Move the mouse to the specified coordinates."""
    controller.position = (x, y)
    time.sleep(get_random_delay(0.01, 0.05))

def click_at(controller: mouse.Controller, x: int, y: int, button: mouse.Button = mouse.Button.left, num_clicks: int = 1) -> None:
    """Click at the given position with optional button and number of clicks."""
    move_to_position(controller, x, y)
    time.sleep(get_random_delay(0.02, 0.1))
    controller.click(button, num_clicks)

def double_click_at(controller: mouse.Controller, x: int, y: int) -> None:
    """Perform a double click at the specified location."""
    click_at(controller, x, y, num_clicks=2)

def press_and_hold(controller: mouse.Controller, x: int, y: int, hold_time: float) -> None:
    """Press and hold the left button for a duration."""
    move_to_position(controller, x, y)
    controller.press(mouse.Button.left)
    time.sleep(hold_time)
    controller.release(mouse.Button.left)

def random_offset_click(controller: mouse.Controller, base_x: int, base_y: int, offset_range: int = 10) -> None:
    """Click near the base position with random offset."""
    offset_x = random.randint(-offset_range, offset_range)
    offset_y = random.randint(-offset_range, offset_range)
    click_at(controller, base_x + offset_x, base_y + offset_y)

def smooth_move(controller: mouse.Controller, x1: int, y1: int, x2: int, y2: int, duration: float = 0.5) -> None:
    """Move mouse smoothly over a duration."""
    steps = max(5, int(duration / 0.01))
    for i in range(steps + 1):
        progress = i / steps
        curr_x = int(x1 + (x2 - x1) * progress)
        curr_y = int(y1 + (y2 - y1) * progress)
        controller.position = (curr_x, curr_y)
        time.sleep(duration / steps)

class MouseAutomationUtils:
    """Collection of utilities for mouse automation after reorganization."""
    def __init__(self) -> None:
        self.controller = mouse.Controller()

    def execute_click(self, x: int, y: int, clicks: int = 1) -> None:
        click_at(self.controller, x, y, num_clicks=clicks)

    def execute_double_click(self, x: int, y: int) -> None:
        double_click_at(self.controller, x, y)

    def execute_hold(self, x: int, y: int, seconds: float) -> None:
        press_and_hold(self.controller, x, y, seconds)

    def execute_random_click(self, x: int, y: int, range_val: int = 5) -> None:
        random_offset_click(self.controller, x, y, range_val)

    def execute_smooth_move(self, start: Tuple[int, int], end: Tuple[int, int], dur: float = 0.5) -> None:
        smooth_move(self.controller, start[0], start[1], end[0], end[1], dur)