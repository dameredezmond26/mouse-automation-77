import time
import random
import math
from typing import List, Tuple

def calculate_click_interval(clicks_per_second: float) -> float:
    """Calculate the time interval between clicks for a given rate."""
    if clicks_per_second <= 0:
        return 1.0
    return 1.0 / clicks_per_second

def add_random_variance(value: float, variance_percent: float = 0.1) -> float:
    """Add a random variance to the base value."""
    if variance_percent < 0:
        variance_percent = 0.0
    delta = value * variance_percent
    return value + random.uniform(-delta, delta)

def is_within_bounds(x: int, y: int, width: int, height: int) -> bool:
    """Verify if the coordinates are inside the given bounds."""
    return 0 <= x < width and 0 <= y < height

def generate_click_intervals(num_clicks: int, min_interval: float, max_interval: float) -> List[float]:
    """Create a list of random intervals for multiple clicks."""
    if num_clicks <= 1:
        return []
    intervals = []
    for _ in range(num_clicks - 1):
        interval = random.uniform(min_interval, max_interval)
        intervals.append(interval)
    return intervals

def human_like_delay(base_delay: float) -> None:
    """Perform a sleep that mimics human timing with variance."""
    delay = add_random_variance(base_delay, 0.2)
    time.sleep(max(0.01, delay))

def convert_to_seconds(milliseconds: int) -> float:
    """Convert a millisecond value to seconds."""
    return milliseconds / 1000.0

def is_valid_click_rate(rate: float) -> bool:
    """Check if the provided click rate is within practical limits."""
    return 0.1 <= rate <= 20.0

def distance_between_points(x1: int, y1: int, x2: int, y2: int) -> float:
    """Compute the straight-line distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generate_smooth_path(start_pos: Tuple[int, int], end_pos: Tuple[int, int], steps: int = 10) -> List[Tuple[int, int]]:
    """Produce a list of positions for a smooth mouse transition."""
    path = []
    sx, sy = start_pos
    ex, ey = end_pos
    for i in range(steps + 1):
        t = i / steps
        curr_x = int(sx + (ex - sx) * t)
        curr_y = int(sy + (ey - sy) * t)
        path.append((curr_x, curr_y))
    return path

def apply_position_jitter(x: int, y: int, amount: int = 3) -> Tuple[int, int]:
    """Slightly randomize a position to avoid detection."""
    new_x = x + random.randint(-amount, amount)
    new_y = y + random.randint(-amount, amount)
    return new_x, new_y