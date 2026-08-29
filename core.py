import time
import threading
from typing import Optional, Dict

try:
    import pyautogui
except ImportError:
    pyautogui = None

class Core:
    """Core module with performance optimized autoclicker logic."""

    def __init__(self, interval: float = 0.1):
        self._is_running = False
        self._worker_thread: Optional[threading.Thread] = None
        self.interval = max(0.001, interval)
        self._click_counter = 0
        self._start_timestamp = 0.0
        self._stats_lock = threading.Lock()

    def _optimized_loop(self):
        """High performance main loop with drift compensation."""
        self._start_timestamp = time.perf_counter()
        next_click_time = self._start_timestamp
        while self._is_running:
            now = time.perf_counter()
            if now >= next_click_time:
                if pyautogui is not None:
                    # Direct click for speed
                    pyautogui.click()
                with self._stats_lock:
                    self._click_counter += 1
                # Update next target, accounts for execution time
                next_click_time += self.interval
            # Calculate remaining time to next click
            remaining = next_click_time - now
            if remaining > 0.002:
                time.sleep(remaining - 0.001)
            elif remaining > 0:
                # Short sleep for precision without high CPU
                time.sleep(0.0005)
            else:
                # Yield CPU if behind schedule
                time.sleep(0)

    def start(self, interval: Optional[float] = None) -> None:
        """Begin the optimized clicking process."""
        if self._is_running:
            return
        if interval is not None:
            self.interval = max(0.001, interval)
        self._is_running = True
        self._click_counter = 0
        self._worker_thread = threading.Thread(
            target=self._optimized_loop, daemon=True
        )
        self._worker_thread.start()

    def stop(self) -> None:
        """Halt the autoclicker and join thread."""
        self._is_running = False
        if self._worker_thread is not None:
            self._worker_thread.join(timeout=1.0)
            self._worker_thread = None

    def get_performance_stats(self) -> Dict[str, float]:
        """Retrieve current performance metrics."""
        with self._stats_lock:
            if self._start_timestamp == 0.0:
                return {"total_clicks": 0, "clicks_per_second": 0.0}
            elapsed = time.perf_counter() - self._start_timestamp
            cps = self._click_counter / elapsed if elapsed > 0 else 0.0
            return {
                "total_clicks": self._click_counter,
                "clicks_per_second": round(cps, 2)
            }

    def update_interval(self, new_interval: float) -> None:
        """Adjust interval for better performance."""
        self.interval = max(0.001, new_interval)