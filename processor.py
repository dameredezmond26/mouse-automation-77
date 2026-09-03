import queue
import threading
import time
from typing import Any, Callable, Dict, Optional


class ClickProcessor:
    """Handles the execution queue for scheduled autoclicker actions."""

    def __init__(self, click_executor: Callable[[int, int, str], None]):
        self._queue: queue.Queue[Dict[str, Any]] = queue.Queue()
        self._is_running = False
        self._thread: Optional[threading.Thread] = None
        self._executor = click_executor

    def start(self) -> None:
        """Starts the background worker thread for processing clicks."""
        if self._is_running:
            return
        self._is_running = True
        self._thread = threading.Thread(target=self._process_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stops the processing loop and clears remaining tasks."""
        self._is_running = False
        if self._thread:
            self._thread.join(timeout=1.0)
        self.clear_queue()

    def queue_click(self, x: int, y: int, button: str = "left", delay: float = 0.0) -> None:
        """Enqueues a click action with an optional pre-delay."""
        self._queue.put({"x": x, "y": y, "button": button, "delay": delay})

    def clear_queue(self) -> None:
        """Removes all pending click events from the queue."""
        while not self._queue.empty():
            try:
                self._queue.get_nowait()
            except queue.Empty:
                break

    def _process_loop(self) -> None:
        """Internal worker loop consuming click tasks from the queue."""
        while self._is_running:
            try:
                task = self._queue.get(timeout=0.1)
                if task["delay"] > 0:
                    time.sleep(task["delay"])
                if self._is_running:
                    self._executor(task["x"], task["y"], task["button"])
                self._queue.task_done()
            except queue.Empty:
                continue
