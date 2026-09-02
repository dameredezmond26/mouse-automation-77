import time
import random
from typing import Callable, Any

def retry_with_backoff(
    operation: Callable[[], Any],
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 30.0,
    jitter: bool = True
) -> Any:
    """
    Execute a network operation with retry logic and exponential backoff.
    """
    last_exception = None
    for attempt in range(max_retries):
        try:
            return operation()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            if attempt == max_retries - 1:
                break
            delay = min(base_delay * (2 ** attempt), max_delay)
            if jitter:
                delay *= (0.5 + random.random())
            time.sleep(delay)
    raise last_exception

# Example network operation function for demonstration
def perform_network_request(url: str) -> str:
    # In real use, this would use requests or urllib
    # Simulating network call
    print(f"Attempting to connect to {url}")
    if random.random() < 0.6:
        raise ConnectionError("Simulated network failure")
    return "Network response received"

if __name__ == "__main__":
    try:
        result = retry_with_backoff(
            lambda: perform_network_request("https://example.com"),
            max_retries=4,
            base_delay=0.5
        )
        print(result)
    except Exception as e:
        print(f"Operation failed after all retries: {e}")