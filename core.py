import time
import threading
from pynput.mouse import Button, Controller

class AutoClicker:
    """Core engine for managing background mouse click automation."""
    
    def __init__(self, interval: float = 0.1, button: Button = Button.left):
        self.interval = interval
        self.button = button
        self.is_clicking = False
        self.is_alive = True
        self.mouse = Controller()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def start(self) -> None:
        """Enable active clicking."""
        self.is_clicking = True

    def stop(self) -> None:
        """Pause active clicking."""
        self.is_clicking = False

    def toggle(self) -> None:
        """Toggle clicking state."""
        self.is_clicking = not self.is_clicking

    def shutdown(self) -> None:
        """Terminate the background thread."""
        self.is_clicking = False
        self.is_alive = False
        if self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _run(self) -> None:
        """Internal execution loop running in a daemon thread."""
        while self.is_alive:
            if self.is_clicking:
                self.mouse.click(self.button)
                time.sleep(self.interval)
            else:
                time.sleep(0.05)
