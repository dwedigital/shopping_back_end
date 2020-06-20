from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
from app import app, routes



if __name__ == '__main__':
    app.run()
