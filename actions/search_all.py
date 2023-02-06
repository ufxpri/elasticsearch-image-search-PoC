from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost'], port='9200')

es.search()
