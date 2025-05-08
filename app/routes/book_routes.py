from flask import Blueprint, Response, abort, make_response, request
from app.models.book import Book
from ..db import db
from .route_utilities import validate_model, create_model, get_models_with_filters

bp = Blueprint("books_bp", __name__, url_prefix="/books")


@bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.put("/<book_id>")
def update_book(book_id):
    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# def validate_book(cls, book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         response = {"message": f"book {book_id} invalid"}
#         abort(make_response(response, 400))

#     query = db.select(Book).where(Book.id == book_id)
#     book = db.session.scalar(query)

#     if not book:
#         response = {"message": f"book {book_id} not found"}
#         abort(make_response(response, 404))

#     return book


@bp.get("/<book_id>")
def get_one_book(book_id):
    # query = db.select(Book).where(Book.id == book_id)
    # book = db.session.scalar(query)

    book = validate_model(Book, book_id)
    # return {
    #     "id": book.id,
    #     "title": book.title,
    #     "description": book.description
    # }
    return book.to_dict()


@bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)

# @bp.get("")
# def get_all_books():
#     query = db.select(Book)

#     title_param = request.args.get("title")
#     if title_param:
#         query = query.where(Book.title.ilike(f"%{title_param}%"))

#     description_param = request.args.get("description")
#     if description_param:
#         query = query.where(Book.description.ilike(f"%{description_param}%"))

#     query = query.order_by(Book.id)
#     # title_param = request.args.get("title")
#     # if title_param:
#     #     query = db.select(Book).where(Book.title.ilike(
#     #         f"%{title_param}%")).order_by(Book.id)
#     # else:
#     #     query = db.select(Book).order_by(Book.id)

#     books = db.session.scalars(query)
#     # We could also write the line above as:
#     # books = db.session.execute(query).scalars()

#     books_response = []
#     for book in books:
#         books_response.append(book.to_dict())
#         # books_response.append(
#         #     {
#         #         "id": book.id,
#         #         "title": book.title,
#         #         "description": book.description
#         #     }
#         # )
#     return books_response


@bp.post("")
def create_book():
    request_body = request.get_json()
    return create_model(Book, request_body)

# @bp.post("")
# def create_book():
#     request_body = request.get_json()

#     try:
#         new_book = Book.from_dict(request_body)

#     except KeyError as error:
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))

#     db.session.add(new_book)
#     db.session.commit()

    # response = {
    #     "id": new_book.id,
    #     "title": new_book.title,
    #     "description": new_book.description,
    # }
    # return response, 201
    return new_book.to_dict(), 201


# @books_bp.post("")
# def create_book():
#     request_body = request.get_json()

#     try:
#         title = request_body["title"]
#         description = request_body["description"]

#         new_book = Book(title=title, description=description)

#     except KeyError as error:
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))

#     db.session.add(new_book)
#     db.session.commit()

#     response = {
#         "id": new_book.id,
#         "title": new_book.title,
#         "description": new_book.description,
#     }
#     return response, 201

# @books_bp.post("")
# def create_book():
#     request_body = request.get_json()
#     title = request_body["title"]
#     description = request_body["description"]

#     new_book = Book(title=title, description=description)
#     db.session.add(new_book)
#     db.session.commit()

#     response = {
#         "id": new_book.id,
#         "title": new_book.title,
#         "description": new_book.description,
#     }
#     return response, 201


# from flask import Blueprint, abort, make_response  # additional imports
# from app.models.book import books

# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# treat a URI the same whether or not it ends in `/`
# @books_bp.get("", strict_slashes=False)
# def get_all_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return books_response


# @books_bp.get("/<book_id>")
# def get_one_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }
# # helper f-n


# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         response = {"message": f"book {book_id} invalid"}
#         abort(make_response(response, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     response = {"message": f"book {book_id} not found"}
#     abort(make_response(response, 404))
""" @books_bp.get("/<book_id>")
def get_one_book(book_id):
    try:
        book_id = int(book_id)
    except ValueError:
        return {"message": f"book {book_id} invalid"}, 400

    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description,
            }

    return {"message": f"book {book_id} not found"}, 404 """
