import logging

def setup_logging(log_file="trading_log.txt"):
    """
    Sets up logging configuration.
    
    :param log_file: Path to the log file
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def write_log(message, level="INFO"):
    """
    Write messages to the log with different levels.
    
    :param message: The log message
    :param level: Log level (INFO, ERROR, etc.)
    """
    if level == "INFO":
        logging.info(message)
    elif level == "ERROR":
        logging.error(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "DEBUG":
        logging.debug(message)
    else:
        logging.info(message)
