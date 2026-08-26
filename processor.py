import time
import logging

logger = logging.getLogger("mouse-automation-77")

class ClickProcessor:
    def __init__(self, config: dict):
        self.config = config
        self.running = False

    def validate_inputs(self) -> bool:
        """Validate autoclicker configuration parameters before execution."""
        interval = self.config.get("interval")
        clicks = self.config.get("clicks")
        button = self.config.get("button")

        if interval is None or not isinstance(interval, (int, float)) or interval < 0:
            logger.error("Invalid interval: must be a non-negative number.")
            return False

        if clicks is None or not isinstance(clicks, int) or clicks < -1:
            logger.error("Invalid clicks: must be an integer >= -1 (-1 for infinite).")
            return False

        if button not in ["left", "right", "middle"]:
            logger.error(f"Invalid mouse button: {button}. Must be left, right, or middle.")
            return False

        return True

    def process_loop(self):
        """Main processing loop with integrated input validation."""
        if not self.validate_inputs():
            logger.critical("Input validation failed. Aborting click process.")
            return

        self.running = True
        interval = self.config["interval"]
        target_clicks = self.config["clicks"]
        executed = 0

        logger.info("Starting autoclicker processing loop.")
        try:
            while self.running:
                if target_clicks != -1 and executed >= target_clicks:
                    logger.info("Target click count reached. Stopping.")
                    break
                
                time.sleep(interval)
                executed += 1
                logger.debug(f"Click executed (#{executed})")
        except Exception as e:
            logger.exception(f"Unexpected error during processing loop: {e}")
        finally:
            self.running = False
            logger.info("Autoclicker processing loop terminated.")
