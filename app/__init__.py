from flask import Flask
from app.config import Config
from flask_dotenv import DotEnv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow



app = Flask(__name__)
env = DotEnv(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
CORS(app, resources={r'*': {'origins': '*'}})
