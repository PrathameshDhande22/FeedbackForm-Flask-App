import os
from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask_pymongo.wrappers import Database

load_dotenv()

mongo = PyMongo()


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.environ.get("MONGODB")
    mongo.init_app(app)
    app.secret_key = os.environ.get("SECRETKEY")

    from .views import home
    app.register_blueprint(home)
    return app


def getdb() -> Database:
    return mongo.db
