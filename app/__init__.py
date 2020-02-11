import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from config import Config

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app


from app import models
