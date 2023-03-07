import numpy as np
import tqdm
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(hosts=['http://localhost'], port='9200')
number_of_docs = 1024

def generate_actions():
    for i in range(number_of_docs):
        document={
            "image_url": "https://picsum.photos/200",
            "embedding": np.random.uniform(0,1,1024).tolist()
        }
        yield document

progress = tqdm.tqdm(unit="docs", total=number_of_docs)
successes = 0
for ok, action in helpers.streaming_bulk(client=es, index="image_feature", actions=generate_actions()):
    progress.update(1)
    successes += ok
    
print(f"Indexed {successes}/{number_of_docs} documents")