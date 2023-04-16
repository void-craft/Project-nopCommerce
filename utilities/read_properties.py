import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'BASE_URL')
        return url

    @staticmethod
    def get_user_email():
        username = config.get('common info', 'USERNAME')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'PASSWORD')
        return password
