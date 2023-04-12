import logging


class LogGen:
    @staticmethod
    def log_gen():
        logger = logging.getLogger()
        file_handler = logging.FileHandler(filename='.\\logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
