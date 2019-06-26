from pymongo import MongoClient

class MongoDBConfig():
    __instance = None

    @staticmethod
    def get_instance():
        if MongoDBConfig.__instance == None:
            MongoDBConfig()
        return MongoDBConfig.__instance

    def __init__(self):
        if MongoDBConfig.__instance != None:
            raise Exception('ERROR: MongoDBConfig is a singleton!')
        else:
            MongoDBConfig.__instance = self

    def open_connection(self):
        self.client = MongoClient('localhost', 27017)

    def get_database(self):
        db = self.client['SoccerOdds']
        return db
