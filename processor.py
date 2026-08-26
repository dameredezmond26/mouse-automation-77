import time
import logging

logger = logging.getLogger('mouse-automation-77')

def process_click_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple[int, int]:
    """Validate and process click coordinates against screen boundaries."""
    try:
        # Ensure inputs are integers
        coord_x = int(x)
        coord_y = int(y)
    except (TypeError, ValueError) as e:
        logger.error(f"Invalid coordinate types provided: x={x}, y={y}. Defaulting to (0, 0).")
        return 0, 0

    # Check for negative values (off-screen)
    if coord_x < 0 or coord_y < 0:
        logger.warning(f"Negative coordinates detected ({coord_x}, {coord_y}). Clamped to boundary 0.")
        coord_x = max(0, coord_x)
        coord_y = max(0, coord_y)

    # Check against maximum screen dimensions
    if coord_x > screen_width or coord_y > screen_height:
        logger.warning(f"Coordinates ({coord_x}, {coord_y}) exceed screen bounds ({screen_width}x{screen_height}). Clamped.")
        coord_x = min(coord_x, screen_width)
        coord_y = min(coord_y, screen_height)

    return coord_x, coord_y

def execute_click_sequence(actions: list, delay: float) -> bool:
    """Safely execute a list of click actions with robust error handling."""
    if not isinstance(actions, list):
        logger.critical("Action sequence must be a valid list.")
        return False

    for index, action in enumerate(actions):
        try:
            if not isinstance(action, dict) or 'x' not in action or 'y' not in action:
                raise KeyError(f"Action at index {index} is missing required keys ('x', 'y').")
            
            time.sleep(max(0.0, float(delay)))
        except (KeyError, TypeError, ValueError) as err:
            logger.error(f"Skipping malformed action at index {index}: {err}")
            continue
        except Exception as unexpected:
            logger.critical(f"Unexpected error during click execution: {unexpected}")
            return False

    return True
