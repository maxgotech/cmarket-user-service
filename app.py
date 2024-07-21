from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]
db.init_app(app)

# view for requests needs to be imported after app ini but before db ini
import userService.view

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
