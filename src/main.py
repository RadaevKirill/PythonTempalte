from src.logger import get_logger

MESSAGE = "Python template is ready. Replace src.main:main with your application entry point."
logger = get_logger(__name__)


def main() -> None:
    logger.info(MESSAGE)


if __name__ == "__main__":
    main()
