from flask import jsonify, request
import uuid
from app import app, db
from app.models import Item
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, desc
import json
# helper class to convert query object to JSON easily
from app.helpers import AlchemyEncoder, update_item


@app.route('/list', methods=['GET', 'POST', 'DELETE'])
def shopping_list():

    if request.method == "POST":
        print("Posted Data")
        post_data = request.get_json()
        item = Item(
            item=post_data.get('item'),
            quantity=post_data.get('quantity'),
            status=post_data.get('bought')
        )
        db.session.add(item)
        db.session.commit()
        return jsonify("Item Added")

    if request.method == "GET":
        all_items = Item.query.all()

        # use the AlchemyEncoder helper class to encode the query object in to JSON
        output = json.dumps(all_items, cls=AlchemyEncoder)
        output = json.loads(output)

        return jsonify({
            "list": output,
            'status': 'success'
    })

    if request.method == 'DELETE':
        Item.query.delete()
        db.session.commit()
        return jsonify("All Deleted")


@app.route('/list/<item_id>', methods=['PUT', 'DELETE'])
def single_item(item_id):
    if request.method == "PUT":
        post_data = request.get_json()

        # update_item is a helper function in helpers.py
        status = update_item(item_id, post_data)
        return jsonify({
            'status': status,
            'Item ID': item_id
        })
    if request.method == "DELETE":
        Item.query.filter_by(id=item_id).delete()
        db.session.commit()
        return jsonify({
            'status': 'Item Deleted',
            'Item ID': item_id
        })




@app.route('/bought/<item_id>', methods=['PUT'])
def bought(item_id):
    if request.method == "PUT":
        item = Item.query.get(item_id)
        print(item)
        item.status = True
        db.session.commit()
        return jsonify({
            'status': 'Update status to bought',
            'Item ID': item_id
        })
