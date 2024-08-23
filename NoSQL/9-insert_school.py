#!/usr/bin/env python3
'''Insert a document in Python'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document into a MongoDB collection.'''
    return mongo_collection.insert(kwargs)
