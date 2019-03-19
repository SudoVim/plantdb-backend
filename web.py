"""
flask API for plantDB
"""

import pymongo
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask("plantdb-api")
CORS(app)

@app.route('/v1/categories/')
def get_categories():
    client = pymongo.MongoClient()
    categories = client.plantdb.categories.find({})

    return jsonify(
        [
            c['name'] for c in categories

        ]

    )

PLANTS_KEYS = [
    "name",
    "latin",
    "category",
    "description",
    "tags",
    "image",

]

@app.route('/v1/plants/')
def get_plants():
    client = pymongo.MongoClient()

    query = {}

    if 'category' in request.args:
        query['category'] = request.args['category']

    if 'tags' in request.args:
        query['$or'] = [
            {
                'tags': t

            } for t in request.args['tags'].split(',')

        ]

    plants = client.plantdb.plants.find(query)
    return jsonify(
        [
            {
                k: p.get(k, None) for k in PLANTS_KEYS

            } for p in plants

        ]

    )
