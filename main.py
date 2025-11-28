from app.logger import get_file_path_logger, setup_logging

logger = get_file_path_logger(__name__)

if __name__ == "__main__":
    setup_logging("app.log")
    logger.info("hello.")
