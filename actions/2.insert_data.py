from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost'], port='9200')

response = es.create(
    index="feature",
    id=3,
    document={
        "name": "ufxpri",
        "message": "the cute and bright person"
    }
)

print(response)