from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost'], port='9200')

response = es.search(
    index="afeature",
    query={
        "match_all": {}
    },
    size=10
)

print(response)