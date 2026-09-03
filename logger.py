import logging
import json
from datetime import datetime
from typing import Dict, Any


class ClickLogger:
    """Utility for logging autoclicker sessions and click telemetry data."""

    def __init__(self, log_file: str = "autoclicker_session.log", verbose: bool = False):
        self.logger = logging.getLogger("mouse_automation_logger")
        self.logger.setLevel(logging.DEBUG if verbose else logging.INFO)
        
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def log_click_event(self, x: int, y: int, button: str, interval: float) -> str:
        """Formats and logs an individual click event."""
        event_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "position": {"x": x, "y": y},
            "button": button,
            "interval_sec": round(interval, 4)
        }
        log_msg = f"CLICK: Pos=({x}, {y}) Button={button} Interval={interval:.4f}s"
        self.logger.info(log_msg)
        return json.dumps(event_data)

    def log_session_summary(self, total_clicks: int, duration_sec: float, target_cps: float) -> Dict[str, Any]:
        """Calculates session stats and outputs summary log."""
        actual_cps = round(total_clicks / duration_sec, 2) if duration_sec > 0 else 0.0
        summary = {
            "total_clicks": total_clicks,
            "duration_seconds": round(duration_sec, 2),
            "target_cps": target_cps,
            "actual_cps": actual_cps
        }
        self.logger.info(
            f"SESSION SUMMARY: Total Clicks={total_clicks} | "
            f"Duration={duration_sec:.2f}s | Avg CPS={actual_cps}"
        )
        return summary
