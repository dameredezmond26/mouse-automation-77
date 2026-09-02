import logging

from logging.handlers import RotatingFileHandler
import os

def setup_rotating_logger(
    logger_name="mouse_automation",
    log_file="logs/automation.log",
    max_size_mb=5,
    backup_count=3,
    level=logging.INFO
):
    """Configure a logger with rotating file handler."""
    # Get or create the logger instance
    logger = logging.getLogger(logger_name)
    # Check for existing handlers to avoid duplicates
    if logger.hasHandlers():
        return logger
    logger.setLevel(level)
    # Prepare the log directory
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # Calculate max bytes for rotation
    max_bytes = max_size_mb * 1024 * 1024
    # Set up the rotating file handler
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(level)
    # Use detailed format for file logs
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    # Add console output for important messages only
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    return logger