import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Constants for logger configuration
LOG_DIRECTORY = "logs"
LOG_FILENAME = "automation.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB per file
BACKUP_COUNT = 3  # Keep 3 backup files

def setup_logger(log_level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with console and rotating file handlers.
    Creates log directory if needed and configures rotation.
    """
    # Ensure log directory exists
    log_dir = Path(LOG_DIRECTORY)
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file_path = log_dir / LOG_FILENAME

    # Get or create logger
    logger = logging.getLogger("mouse_automation_77")
    logger.setLevel(log_level)

    # Avoid adding duplicate handlers on multiple calls
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler for real-time output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # Rotating file handler for persistent logs
    file_handler = RotatingFileHandler(
        filename=str(log_file_path),
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
    )
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    logger.info("Logger initialized with rotation")
    return logger

# Default logger instance for easy import and use
logger = setup_logger()