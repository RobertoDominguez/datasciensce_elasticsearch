from elasticsearch import Elasticsearch
import os

ELASTICSEARCH_PROTOCOL=os.getenv('ELASTICSEARCH_PROTOCOL')
URL_ELASTICSEARCH=os.getenv('ELASTICSEARCH_DB')


class ElasticSearchPDO:

    def __init__(self):
        # Connect to Elasticsearch
        self.es = Elasticsearch(
            hosts=[ELASTICSEARCH_PROTOCOL+URL_ELASTICSEARCH],
            #basic_auth=("usuario", "contraseña")
        )


    # Crear un índice (si no existe)
    def create_index(self,index_name) -> bool:
        if not self.es.indices.exists(index=index_name):
            self.es.indices.create(index=index_name)
            return True
        else:
            print(f"Index '{index_name}' already exists.")
            return False

    # Create a document
    def create_document(self,index_name, doc_id, document):
        response = self.es.index(index=index_name, id=doc_id, document=document)
        return response

    # Get a document by ID
    def get_document(self,index_name, doc_id):
        try:
            response = self.es.get(index=index_name, id=doc_id)
            return response["_source"]
        except Exception as e:
            print("Error getting document:", e)

    # Update a document
    def update_document(self,index_name, doc_id, document):
        try:
            response = self.es.update(index=index_name, id=doc_id, doc=document)
            return response
        except Exception as e:
            print("Error updating document:", e)

    # Delete a document
    def delete_document(self,index_name, doc_id):
        try:
            response = self.es.delete(index=index_name, id=doc_id)
            return response
        except Exception as e:
            print("Error deleting document:", e)

    def search(self,index_name,query):
        return self.es.search(index=index_name, query=query)