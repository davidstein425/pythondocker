# user_api/main.py

import os
import datetime
from config import app_config
from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    import models
    # TODO: Figure out import issue with import models here and import of db in models.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/users', methods=['POST'])
    def create_user():
        content = request.json
        email_address = content["email"]
        pwd = content["password"]

        user = models.User(email=email_address, password=pwd, inserted_on=datetime.datetime.now(),
                           updated_on=datetime.datetime.now())
        db.session.add(user)
        db.session.commit()

        return jsonify({"Success": "OK", "Email": email_address})

    return app

app = create_app()


if __name__ == '__main__':
    app.run()








