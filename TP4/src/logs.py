import logging
import os

class Logger:
    def __init__(self,filePath="TP4/logs.log", withConsole=True):
        # Create if not exist
        if not os.path.exists(os.path.dirname(filePath)):
            os.makedirs(os.path.dirname(filePath))
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
        file_handler = logging.FileHandler(filePath)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        if withConsole:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(stream_handler)

    def emergency(self,message):
        self.logger.critical(message)

    def alert(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)

    def error(self,message):
        self.logger.error(message)

    def warning(self,message):
        self.logger.warning(message)

    def notice(self,message):
        self.logger.info(message)

    def info(self,message):
        self.logger.info(message)

    def debug(self,message):
        self.logger.debug(message)

