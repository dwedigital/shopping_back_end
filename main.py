from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
from app import app, routes, socketio



if __name__ == '__main__':
    socketio.run(app)
