import time
import random
import requests
from typing import Any, Callable, Optional

class NetworkRetryHandler:
    """Handles retry logic for network operations with exponential backoff."""

    def __init__(self, max_retries: int = 5, initial_delay: float = 1.0, max_delay: float = 30.0):
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay

    def execute(self, operation: Callable[[], Any], *args, **kwargs) -> Optional[Any]:
        """Execute network operation with retries on failure."""
        delay = self.initial_delay
        last_exception = None
        for attempt in range(1, self.max_retries + 1):
            try:
                result = operation(*args, **kwargs)
                return result
            except (requests.exceptions.RequestException, ConnectionError, TimeoutError) as e:
                last_exception = e
                if attempt == self.max_retries:
                    break
                # Apply jitter for randomized delay to avoid synchronized retries
                jitter = random.uniform(0, 0.5)
                sleep_time = min(delay + jitter, self.max_delay)
                time.sleep(sleep_time)
                delay *= 2
        if last_exception:
            raise last_exception
        return None

# Example network operation for fetching automation settings
def fetch_automation_settings(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

# Practical usage example
if __name__ == "__main__":
    handler = NetworkRetryHandler(max_retries=3)
    try:
        settings = handler.execute(fetch_automation_settings, "https://example.com/api/settings")
        print("Successfully retrieved settings:", settings)
    except Exception as e:
        print(f"Network operation failed after all retries: {e}")