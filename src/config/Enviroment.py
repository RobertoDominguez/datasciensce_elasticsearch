import os
from dotenv import load_dotenv


class Enviroment:
    def __init__(self):
        load_dotenv()
        return
    
    #----------------API ENV-------------------------
    def getAPIDatabases(self):
        return os.getenv("API_DATABASES")
    
    def getDatabaseNames(self):
        return { '1' : 'Company 1', '2': 'Company 2'}
    
    def getAPIToken(self):
        return os.getenv("API_TOKEN")
    
    def getAPIProtocol(self):
        return os.getenv("API_PROTOCOL")
    
    def getAPIHost(self):
        return os.getenv("API_HOST")
    
    #----------------ELASTIC SEARCH ENV--------------
    def getElasticSearchProtocol(self):
        return os.getenv("ELASTICSEARCH_PROTOCOL")
    
    def getElasticSearchDB(self):
        return os.getenv("ELASTICSEARCH_DB")
    
    def getElasticSearchPassword(self):
        return os.getenv("ELASTICSEARCH_PASSWORD")