from flask import Flask
from .db import db, migrate
from .models import book, author
# from .routes.book_routes import bp
# from .routes import book_routes
from .routes.book_routes import bp as books_bp
from .routes.author_routes import bp as authors_bp
import os


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
    # app.register_blueprint(book_routes.bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(authors_bp)

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
