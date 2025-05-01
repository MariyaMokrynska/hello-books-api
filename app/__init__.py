from flask import Flask
from .db import db, migrate
from .models import book
from .routes.book_routes import books_bp
import os
from dotenv import load_dotenv

load_dotenv()


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app


# from flask import Flask
# # from .routes.hello_world_routes import hello_world_bp
# from .db import db, migrate
# from .models import book  # Newly added import
# from .routes.book_routes import books_bp


# def create_app():
#     app = Flask(__name__)

#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

#     db.init_app(app)
#     migrate.init_app(app, db)

#     # Register Blueprints here
# #    app.register_blueprint(hello_world_bp)
#     app.register_blueprint(books_bp)

#     return app
