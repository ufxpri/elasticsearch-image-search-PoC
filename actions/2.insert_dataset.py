import numpy as np
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost'], port='9200')

for i in range(1024):
    response = es.create(
        index="new_feature",
        id=i,
        document={
            "image_url": "https://picsum.photos/200",
            "embedding": np.random.uniform(0,1,1024).tolist()
        }
    )

    print(response)
