from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost'], port='9200')

es.indices.delete(index="new_feature", ignore=404)

es.indices.create(
    index="new_feature", 
    settings={
        "number_of_shards": 1
    },
    mappings={
        "properties": {
            "embedding": {
                "type": "dense_vector",
                "dims": 1024,
                "index": True,
                "similarity": "dot_product" 
            },
            "image_url": {
                "type": "text"
            }
        }
    }, 
    params=None, 
    headers=None
)

print(es.indices.get(index='new_feature'))