#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from server.models import db, Employee, Onboarding, Review  # fixed import

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    db.init_app(app)
    Migrate(app, db)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(port=5555, debug=True)
