# import dataset.getter

from utils.ElasticSearchPDO import ElasticSearchPDO

indexNameTest='test'
docID='1'

print(ElasticSearchPDO().create_index(index_name=indexNameTest))
print(ElasticSearchPDO().create_document(index_name=indexNameTest,doc_id=docID ,document={'1':'Dato'}))
print(ElasticSearchPDO().update_document(index_name=indexNameTest,doc_id=docID ,document={'1':'Edicion'}))
print(ElasticSearchPDO().get_document(index_name=indexNameTest, doc_id=docID))

# print(ElasticSearchPDO().search(index_name="attendance_facts", query={"match": {"worked_minutes": str("0")}}))