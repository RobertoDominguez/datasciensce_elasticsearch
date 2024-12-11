from controllers.getter.GetterController import GetterController

# This file inserts the data obtained by the API Service to Elasticsearch
def migrate():
    GetterController().migrate()

migrate()