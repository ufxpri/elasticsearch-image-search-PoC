import numpy as np
from elasticsearch import Elasticsearch
np.random.seed(0)

es = Elasticsearch(hosts=['http://localhost'], port='9200')

response = es.search(
    index="new_feature",
    query={
        "function_score": {
            "query": {
                "match_all": {}
            },
            "script_score": {
                "script": {
                    "source": "1 / (1 + l2norm(params.query_vector, 'embedding'))",
                    "params":{
                        "query_vector": np.random.uniform(0,1,1024).tolist()
                    }
                }
            }
        }
    }
)

# print(response)

response['took']
response['timed_out']
response['_shards']
response['hits']['total']
response['hits']['max_score']
response['hits']['hits']

for hit in response['hits']['hits']:
    hit['_index']
    hit['_type']
    hit['_id']
    hit['_score']
    hit['_source']
    print(hit['_id'], hit['_score'], hit['_source']['image_url'])