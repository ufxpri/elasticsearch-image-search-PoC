from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost'], port='9200')

es.indices.delete(index="new_feature")

es.indices.create(
    index="new_feature", 
    settings={
        "number_of_shards": 1
    },
    mappings={
        "properties": {
            "feature": {
                "type": "dense_vector",
                "dims": 128
            },
            "image_id": {
                "type": "text"
            }
        }
    }, 
    params=None, 
    headers=None,
    ignore=400
)

print(es.indices.get(index='new_feature'))