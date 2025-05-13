import logging

class Logger:
    # Config, free to edit
    _timestamp = True
    _log_level = True
    
    _logger = None

    @classmethod
    def _get_logger(cls):
        if cls._logger is None:
            cls._logger = logging.getLogger("my_logger")
            cls._logger.setLevel(logging.DEBUG)
            if not cls._logger.handlers:
                ch = logging.StreamHandler()
                ch.setLevel(logging.DEBUG)
                
                base_format = []
                if cls._timestamp: base_format.append('[%(asctime)s]')
                if cls._log_level: base_format.append('[%(levelname)s]')
                
                base_format.append('%(message)s')
                base_format = " ".join(base_format)
                
                custom_formatter = logging.Formatter(base_format, datefmt='%Y-%m-%d %H:%M:%S')
                ch.setFormatter(custom_formatter)
                cls._logger.addHandler(ch)
        return cls._logger

    @classmethod
    def info(cls, message):
        cls._get_logger().info(message)

    @classmethod
    def warn(cls, message):
        cls._get_logger().warning(message)

    @classmethod
    def error(cls, message):
        cls._get_logger().error(message)

    @classmethod
    def debug(cls, message):
        cls._get_logger().debug(message)

