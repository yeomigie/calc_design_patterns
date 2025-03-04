import logging
import logging.config

# Load logging configuration
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

# Example logging
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
