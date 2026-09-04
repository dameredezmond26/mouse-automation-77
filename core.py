import time
import requests
from functools import wraps
from typing import Callable, Any

def retry_on_failure(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry network operations on failure."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
                        continue
            raise last_exception
        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, delay=2)
def fetch_remote_config(url: str) -> dict:
    """Fetches remote configuration with built-in retry logic."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

def run_autoclicker_sync():
    """Syncs configuration before starting automation cycle."""
    config_url = "https://api.mouse-automation-77.io/v1/settings"
    try:
        settings = fetch_remote_config(config_url)
        print(f"Sync successful: {settings.get('version')}")
    except Exception as err:
        print(f"Fatal sync error: {err}")