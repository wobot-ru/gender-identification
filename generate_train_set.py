# -*- coding: utf-8 -*-
import codecs
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://91.210.104.87:9200'])

total = 40000
half = total / 2


def query(gender):
    return {
        "size": 0,
        "query": {
            "term": {
                "profile_gender": {
                    "value": gender
                }
            }
        },
        "aggs": {
            "agg_profile": {
                "terms": {
                    "field": "profile_name",
                    "size": total
                }
            }
        }
    }


def dump_male():
    q = query('M')
    res = es.search(index="wobot31", body=q)
    buckets = res['aggregations']['agg_profile']['buckets']
    f_train = codecs.open('male_train.txt', 'w', 'utf-8')
    for b in buckets[:half]:
        f_train.write(b['key'] + '\r\n')

    f_test = codecs.open('male_test.txt', 'w', 'utf-8')
    for b in buckets[half:]:
        f_test.write(b['key'] + '\r\n')


def dump_female():
    q = query('W')
    res = es.search(index="wobot31", body=q)
    buckets = res['aggregations']['agg_profile']['buckets']

    f_train = codecs.open('female_train.txt', 'w', 'utf-8')
    for b in buckets[:half]:
        f_train.write(b['key'] + '\r\n')

    f_test = codecs.open('female_test.txt', 'w', 'utf-8')
    for b in buckets[half:]:
        f_test.write(b['key'] + '\r\n')


dump_male()
dump_female()
