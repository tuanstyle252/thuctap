import configparser

config = configparser.RawConfigParser()
configFilePath = 'E:/thuctap/Configuration/config.ini'
config.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password