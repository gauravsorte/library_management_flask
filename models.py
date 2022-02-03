from flask_sqlalchemy import SQLAlchemy
from main import db



class Members(db.Model):
    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    phone_number = db.Column(db.String(45), nullable = False)
    no_of_books_issued = db.Column(db.Integer)
    late_fee = db.Column(db.Integer)

class Issued_Books(db.Model):
    issue_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    issue_date = db.Column(db.String(45))
    issue_time = db.Column(db.String(45))
    return_date = db.Column(db.String(45))

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    author = db.Column(db.String(45), nullable=False)
    average_rating = db.Column(db.String(45))
    isbn = db.Column(db.Integer)
    isbn13 = db.Column(db.Integer)
    number_of_pages = db.Column(db.Integer)
    publication_date = db.Column(db.String(45))
    publisher = db.Column(db.String(45))
    language_code = db.Column(db.String(45))
    total_book_count = db.Column(db.Integer, nullable=False)
    available_book_count = db.Column(db.Integer, nullable=False)


class Transctions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    issued_or_returned = db.Column(db.String(45))
    total_quantity = db.Column(db.Integer)
    transaction_date = db.Column(db.String(45))
    transaction_time = db.Column(db.String(45))

