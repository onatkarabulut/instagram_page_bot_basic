import logging

class Logger:
    def __init__(self, logger_name='BotLogger'):
        self.logger = logging.getLogger(logger_name)
        logging.basicConfig(filename='Log/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        self.logger.setLevel(logging.INFO)

    def set_log(self, text, level=logging.INFO):
        decorated_text = self.decorate_text(text)
        if level == logging.INFO:
            self.logger.info(decorated_text)
        elif level == logging.ERROR:
            self.logger.error(decorated_text)
        elif level == logging.WARNING:
            self.logger.warning(decorated_text)
        elif level == logging.DEBUG:
            self.logger.debug(decorated_text)
        elif level == logging.CRITICAL:
            self.logger.critical(decorated_text)

    def decorate_text(self, text):
        return f"================ {text} ================"
