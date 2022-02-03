from crypt import methods
import re
from textwrap import indent
import types
from xml.dom.minidom import Attr
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
import json

import datetime
# from models import *
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/library_management'
db = SQLAlchemy(app)




id_dictionary = {'g_member_id': 10001, 'g_issue_id': 10075, 'g_transaction_id': 20075}



class Members(db.Model):
    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    phone_number = db.Column(db.String(45), nullable = False)
    no_of_books_issued = db.Column(db.Integer)
    late_fee = db.Column(db.Integer)
    total_fees_paid = db.Column(db.Integer)


class Issuedbooks(db.Model):
    issue_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    issue_date = db.Column(db.String(45))
    issue_time = db.Column(db.String(45))
    # return_date = db.Column(db.String(45))

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    author = db.Column(db.String(45))
    average_rating = db.Column(db.String(45))
    isbn = db.Column(db.String(20))
    isbn13 = db.Column(db.String(20))
    number_of_pages = db.Column(db.Integer)
    publication_date = db.Column(db.String(45))
    publisher = db.Column(db.String(45))
    language_code = db.Column(db.String(45))
    total_book_count = db.Column(db.Integer)
    available_book_count = db.Column(db.Integer)
    no_of_times_issued = db.Column(db.Integer)



class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    t_member_id = db.Column(db.Integer)
    t_book_id = db.Column(db.Integer)
    issued_or_returned = db.Column(db.String(45))
    total_quantity = db.Column(db.Integer)
    transaction_date = db.Column(db.String(45))
    transaction_time = db.Column(db.String(45))




@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/importBooks')
def import_books():
    api = 'https://frappe.io/api/method/frappe-library?page=1&title=harry'
    books = json.loads(json.dumps(requests.get(api).json(), indent = 5))

    already_added_books = []

    for list_ in books['message']:
        print(list_['bookID'])
        book_id = list_['bookID']
        title = list_['title']
        author = list_['authors']
        avg_rating = list_['average_rating']
        isbn = list_['isbn']
        isbn13 = list_['isbn13']
        no_pages = list_['  num_pages']
        pub_date = list_['publication_date']
        publisher = list_['publisher']
        lang_code = list_['language_code']
        tot_books = 0
        ava_books = 0
        if isbn in already_added_books:
            continue
        else:
            entry = Books(book_id=book_id, title = title, author = author, average_rating = avg_rating, isbn = isbn, isbn13 = isbn13, number_of_pages = no_pages,publication_date=pub_date, publisher=publisher, language_code=lang_code, total_book_count=tot_books, available_book_count=ava_books)
            try:
                db.session.add(entry)
                db.session.commit()
            except Exception as e:
                # session.rollback()
                print('---------------------------- ', e)
                raise
            else:
                already_added_books.append(isbn)
                print('>>>>>>>>>>>>>>>> Accepted....')
    return redirect('/viewBooks')

@app.route('/addBook', methods=['GET', 'POST'])
def add_books():
    if request.method == 'POST':
        book_id = request.form.get('bookId')
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        isbn13 = request.form.get('isbn13')
        no_of_pages = request.form.get('noPages')
        publcation_date = request.form.get('pub_date')
        publisher = request.form.get('publisher')
        language_code = request.form.get('language_code')
        total_quantity = request.form.get('total_quantity')
        available_quantity = request.form.get('available_quantity')


        entry = Books(book_id=book_id, title = title, author = author, average_rating = 4, isbn = isbn, isbn13 = isbn13, number_of_pages = no_of_pages,publication_date=publcation_date, publisher=publisher, language_code=language_code, total_book_count=total_quantity, available_book_count=available_quantity)
        try:
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
                # session.rollback()
            print('---------------------------- ', e)
            raise
        else:
            print('>>>>>>>>>>>>>>>> Accepted....')
        return redirect('/viewBooks')

    return render_template('addBook.html')


@app.route('/viewBooks')
def view_books():
    try:
        books = Books.query.all()
        for i in books:
            print(vars(i))
            print(i.book_id)
            print(i.title)
            print(i.author)

    except Exception as e:
        print(e)
    
    return render_template('viewBooks.html', books=books)


@app.route('/editBook/<string:id>', methods=['GET', 'POST'])
def editBooks(id):
    if request.method == 'POST':
        book = Books.query.filter_by(book_id = id).first()

        book.book_id = request.form.get('bookId')
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.isbn = request.form.get('isbn')
        book.isbn13 = request.form.get('isbn13')
        book.number_of_pages = request.form.get('noPages')
        book.publcation_date = request.form.get('pub_date')
        book.publisher = request.form.get('publisher')
        book.language_code = request.form.get('language_code')
        book.total_book_count = request.form.get('total_quantity')
        book.available_book_count = request.form.get('available_quantity')

        try:
            db.session.commit()
        except Exception as e:
            print('---------------------------- ', e)
            raise
        else:
            print('>>>>>>>>>>>>>>>> Accepted....')
        return redirect('/viewBooks')

    else:
        book = Books.query.filter_by(book_id = id).first()

        if book:
            return render_template('editBook.html', book = book)
        else:
            return 'No Book Found'


@app.route('/deleteBook/<string:id>')
def delete_book(id):
    book = Books.query.filter_by(book_id=id).first()
    print('>>>>>>>>>>>>>>>>>>>>> ',book)
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
    else:
        print('----------------------------- deletion sucessful')
    return redirect('/viewBooks')


# =================================================================================================================

@app.route('/addMember', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        f_name = request.form.get('firstName')
        l_name = request.form.get('lastName')
        # id = request.form.get('memberId')
        phone_no = request.form.get('phoneNumber')
        print('>>>>', type(f_name), l_name, id, phone_no)
        entry = Members( first_name = f_name, last_name = l_name, phone_number = phone_no, no_of_books_issued=0, late_fee=0)
        try:
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            print(e)
        else:
            # session.close()
            print('ok')
            return redirect('/viewMembers')
    else: 
        print('GET')
        
    return render_template('addmember.html')


@app.route('/viewMembers')
def view_members():
    members = {}
    try:
        members = Members.query.all()
    except Exception as e:
        print(e)
    
    return render_template('viewmembers.html', member=members)



@app.route('/editMember/<string:id>', methods=['GET', 'POST'])
def editMembers(id):
    if request.method == 'POST':
        member = Members.query.filter_by(member_id=id).first()

        member.first_name = request.form.get('firstName')
        member.last_name = request.form.get('lastName')
        # member.member_id = request.form.get('memberId')
        member.phone_number = request.form.get('phoneNumber')
        try:
            db.session.commit()
        except Exception as e:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
        return redirect('/viewMembers')
    else: 
        member = Members.query.filter_by(member_id=id).first()
        try:
            # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>> ',member.member_id)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>> ',vars(member))
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>> ',member.first_name)


        except Exception as e:
            print('------------------------------- ',e)
        if(member):
            return render_template('editMember.html', member=member)
        else:
            return 'No Member Found'
    # return 'TRUE'


@app.route('/deleteMember/<string:id>')
def delete_member(id):
    member = Members.query.filter_by(member_id=id).first()
    print('>>>>>>>>>>>>>>>>>>>>> ',member)
    try:
        db.session.delete(member)
        db.session.commit()
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
    else:
        print('----------------------------- deletion sucessful')
    return redirect('/viewMembers')



# todo: ===================================================================================================================

@app.route('/issueBook/<string:i_member_id>', methods=["GET", "POST"])
def issue_book(i_member_id):
    if request.method == 'POST':
        # issue_id = id_dictionary['g_issue_id']
        member_id = i_member_id
        book_id = request.form.get('selected_book_id') 
        issue_date = datetime.date.today().strftime('%d-%m-%Y')
        issue_time = datetime.datetime.now().strftime('%H:%M:%S')

        book = Books.query.filter_by(book_id = book_id).first()

        if(book.available_book_count > 0):
            try:
            
                entry = Issuedbooks( member_id=member_id, book_id=book_id, issue_date=issue_date, issue_time=issue_time)
                try:
                    db.session.add(entry)
                    db.session.commit()
                except Exception as e:
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)

            except Exception as e:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ',e)
            else:
                # trans_id = id_dictionary['g_transaction_id']
                try:
                    new_entry = Transactions( t_book_id=book_id , t_member_id=i_member_id, issued_or_returned='Issued', total_quantity=1,transaction_date=issue_date, transaction_time=issue_time)
                    # db.session.close()
                    db.session.add(new_entry)
                    db.session.commit()
                except Exception as e:
                    print('transaction >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ',e)

            finally:
                id_dictionary['g_transaction_id'] += 2
                id_dictionary['g_issue_id'] += 2

            try:
                book.available_book_count -= 1
                book.no_of_times_issued += 1
                # db.session.close()
                db.session.commit()

            except Exception as e:
                print('book update >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',e)

            try:
                # book__ = Issuedbooks.query.filter_by(member_id = i_member_id).first()
                mem = Members.query.filter_by(member_id = i_member_id).first()
                # print(type(book__))
                # print(len(book__[0]))
                mem.no_of_books_issued += 1
                db.session.commit()
            except Exception as e:
                print('Book Exception in issue book >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',e)

            return redirect('/viewMembers')
        else:
            return 'Book Not Available'
    else:
        books = Books.query.all()
        member = Members.query.filter_by(member_id = i_member_id).first()
        return render_template('issueBook.html', books = books, member = member)



@app.route('/issuedBooks')
def issuedBooks():
    members_list = []
    try:
        issued_books = Issuedbooks.query.all()
        print(issued_books[0].member_id)
        for i in range(len(issued_books)):
            id_ = issued_books[i].member_id
            m = Members.query.filter_by(member_id= id_).first()
            s = m.first_name +' '+ m.last_name
            members_list.append(s)
        print('>>>>>>>>>>>>>>>>>>', members_list)

    except Exception as e:
        print('issued book >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
    return render_template('issuedBooks.html', issued_books=issued_books, members = members_list, len_= len(issued_books))


@app.route('/memberIssuedBooks/<string:m_id>', methods=['GET', "POST"])
def member_issued_books(m_id):
    try:
        i_books = Issuedbooks.query.filter_by(member_id = m_id)
        print(i_books[0].book_id)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)

    return render_template('memberIssuedBooks.html', books = i_books)

# ===================================================================================================

@app.route('/returnBook/<string:issue_id>/<string:member_id>/<string:book_id>/<string:fees>', methods=['GET', 'POST'])
def return_book(issue_id, member_id, book_id, fees):
    if request.method == 'POST':
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> in return book')
        return_date = datetime.date.today().strftime('%d-%m-%Y')
        return_time = datetime.datetime.now().strftime('%H:%M:%S')
        amount_paid = request.form.get('amount_paid')
        try:
            member = Members.query.filter_by(member_id=member_id).first()
            issued_book = Issuedbooks.query.filter_by(issue_id = issue_id).first()
            book = Books.query.filter_by(book_id = book_id).first()


            member.no_of_books_issued -= 1
            member.late_fee = int(fees) - int(amount_paid)
            member.total_fees_paid = int(member.total_fees_paid) + int(amount_paid)
            try:
                db.session.commit()
            except Exception as e:
                print('updating at return >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
            
            entry = Transactions( t_member_id=member_id, t_book_id=book_id, issued_or_returned='Returned', total_quantity = 1, transaction_date=return_date, transaction_time=return_time)
            try:
                db.session.add(entry)
                db.session.commit()
            except Exception as e:
                print('transaction return update >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
        

            try:
                db.session.delete(issued_book)
                db.session.commit()
            except Exception as e:
                print('return issue book >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)


            try:
                book.available_book_count += 1
                
                db.session.commit()
            except Exception as e:
                print('return book quantity update >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
        
        except Exception as e:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', e)
            
        else:
            id_dictionary['g_transaction_id'] += 2
        
    return redirect('/viewMembers')

@app.route('/returnBookDetails/<string:r_issue_id>/<string:r_member_id>/<string:r_book_id>')
def return_book_details(r_issue_id, r_member_id, r_book_id):
    member = Members.query.filter_by(member_id=r_member_id).first()
    book = Books.query.filter_by(book_id = r_book_id).first()
    issued_book = Issuedbooks.query.filter_by(issue_id = r_issue_id).first()
    error = False
    t_date = datetime.date.today() 
    # date_ =  datetime.datetime.strptime(issued_book.issue_date, '%d-%m-%y').date()
    # date = issued_book.issue_date.split('-')
    # i_date = date[2]+'-' + date[1]+ '-' + date[0]
    # print(type(issued_book.issue_date))
    date_ = datetime.datetime.strptime(issued_book.issue_date, '%d-%m-%Y')
    # return_date = datetime.datetime.strptime(issued_book.issue_date, '%d-%m-%y').date()
    
    date_ = date_.date()
    print(  t_date)
    print((t_date - date_).days)
    rented_date = (t_date - date_).days
    total_fees = rented_date * 5 + member.late_fee
    

    return render_template('returnBookDetails.html',error=error, book = book, member=member, issued_book = issued_book, fees = total_fees) 



@app.route('/transactions')
def show_transactions():
    transactions = Transactions.query.all()

    
    return render_template('transactions.html', transactions=transactions)


@app.route('/reports_')
def report_page():
    books = Books.query.all()
    members = Members.query.all()
    most_issued_book = 0
    most_issued_book_count = 0
    highest_paid_member = 0
    highest_paid_fees = 0
    for i in books:
        if(int(i.no_of_times_issued) > int(most_issued_book_count)):
            most_issued_book_count = int(i.no_of_times_issued)
            most_issued_book = i

    for i in members:
        if(int(i.total_fees_paid) > int(highest_paid_fees)):
            highest_paid_fees = int(i.total_fees_paid)
            highest_paid_member = i

    
    return render_template('report.html', book = most_issued_book, member = highest_paid_member)

app.run(debug=True)