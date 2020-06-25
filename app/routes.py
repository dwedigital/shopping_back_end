from flask import request
import json
from app import app, db, socketio
from app.models import Item
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, desc
# helper class to convert query object to JSON easily
from app.helpers import AlchemyEncoder, update_item
from flask_socketio import send, emit

@socketio.on('connect')
def handle_message():
    print(request.sid)

@socketio.on('getList')
def getList():
    all_items = Item.query.all()
    # use the AlchemyEncoder helper class to encode the query object in to JSON
    output = json.dumps(all_items, cls=AlchemyEncoder)
    output = json.loads(output)
    socketio.emit('updateList', output)


@socketio.on('clearList')
def clearList():
    Item.query.delete()
    db.session.commit()
    getList()


@socketio.on('boughtItem')
def boughtItem(payload):
    print(payload)
    item = Item.query.get(payload['id'])
    item.status = payload['status']
    db.session.commit()
    getList()


@socketio.on('deleteItem')
def deleteItem(itemID):
    Item.query.filter_by(id=itemID).delete()
    db.session.commit()
    getList()


@socketio.on('updateItem')
def updateItem(payload):
    item = Item.query.get(payload['id'])
    item.item = payload.get("item")
    item.quantity = payload.get("quantity")
    db.session.commit()
    getList()


@socketio.on('addItem')
def addItem(payload):
    print((payload))
    emit('testEmit', payload, broadcast=True)
    item = Item(
        item=payload['item'],
        quantity=payload['quantity'],
        status=False
    )
    db.session.add(item)
    db.session.commit()
    print('item added')
    getList()
