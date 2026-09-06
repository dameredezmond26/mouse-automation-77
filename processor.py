import json
from typing import Dict, List, Any


class ClickProfileProcessor:
    """Processes, validates, and formats autoclicker sequence profile data."""

    VALID_BUTTONS = {"left", "right", "middle"}

    def __init__(self, default_delay_ms: int = 100):
        self.default_delay_ms = default_delay_ms

    def validate_click_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Validates coordinates, click button type, and delay parameters."""
        x = int(event.get("x", 0))
        y = int(event.get("y", 0))
        if x < 0 or y < 0:
            raise ValueError(f"Invalid coordinates ({x}, {y}): values must be non-negative")

        button = str(event.get("button", "left")).lower()
        if button not in self.VALID_BUTTONS:
            raise ValueError(f"Unsupported mouse button '{button}'")

        try:
            delay_ms = max(0, int(event.get("delay_ms", self.default_delay_ms)))
        except (ValueError, TypeError):
            delay_ms = self.default_delay_ms

        return {
            "x": x,
            "y": y,
            "button": button,
            "delay_ms": delay_ms,
            "double_click": bool(event.get("double_click", False))
        }

    def process_sequence(self, raw_events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Processes a list of raw click actions into a validated execution script."""
        validated_events = [self.validate_click_event(evt) for evt in raw_events]
        total_duration = sum(evt["delay_ms"] for evt in validated_events)
        click_count = len(validated_events)

        return {
            "summary": {
                "total_clicks": click_count,
                "total_duration_ms": total_duration,
                "average_delay_ms": (total_duration / click_count) if click_count > 0 else 0.0
            },
            "events": validated_events
        }

    def save_profile(self, raw_events: List[Dict[str, Any]], filepath: str) -> None:
        """Validates sequence payload and saves formatted profile to JSON."""
        processed_data = self.process_sequence(raw_events)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(processed_data, f, indent=2)
