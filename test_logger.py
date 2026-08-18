from logger import get_logger


def test_logger_creation():
    logger = get_logger("test_logger")

    assert logger is not None
    assert logger.name == "test_logger"


def test_logger_level():
    logger = get_logger("test_logger_level")

    assert logger.level > 0
