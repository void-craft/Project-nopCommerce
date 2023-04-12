import configparser

CONFIG = configparser.RawConfigParser()
CONFIG.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = CONFIG.get('common info', 'baseUrl')
        return url

    @staticmethod
    def get_user_email():
        username = CONFIG.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = CONFIG.get('common info', 'password')
        return password
