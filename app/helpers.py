from sqlalchemy.ext.declarative import DeclarativeMeta
import json
from app.models import Item
from app import db


# Class used to 'jsonify' sqlalchemy queries
class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    # this will fail on non-encodable values, like other classes
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

# Method used to update items 
def update_item(item_id, post_data):
    print(post_data)
    item = Item.query.get(item_id)
    item.item = post_data.get("item")
    item.quantity = post_data.get("quantity")
    db.session.commit()
    return (f"ID {item_id}-{item.item} updated")
