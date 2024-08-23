#!/usr/bin/env python3
'''Insert a document in Python'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document into a MongoDB collection.'''
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
