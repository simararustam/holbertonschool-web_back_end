#!/usr/bin/env python3
'''
Write a Python function that returns the list
of school having a specific topic:
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
    '''
    return [collection for collection in mongo_collection.find(
        {"topics": topic}
        )]
