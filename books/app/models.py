#!/usr/bin/python3
# Models for Books Microservice
'''
 Author: Daniel Córdova A.
'''

from app import db

class BookType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), index=True, unique=True, nullable=False)
    genres = db.relationship('BookGenre', backref='gender_type', lazy='dynamic')
    book = db.relationship('Book', backref='type', lazy='dynamic')

    def json_dump(self):
        return dict(id=self.id, type=self.type)

    def __repr__(self):
        return '<BookType %r>' % (self.type)

class BookGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), index=True, nullable=False)
    type = db.Column(db.String(100), db.ForeignKey('book_type.type'), nullable=False)
    book = db.relationship('Book', backref='gender', lazy='dynamic')

    def json_dump(self):
        return dict(id=self.id, genre=self.genre, type=self.type)

    def __repr__(self):
        return '<BookGenre %r>' % (self.genre)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, nullable=False)
    lastname = db.Column(db.String(150), index=True, nullable=False)
    book_author_name = db.relationship('Book', backref='name', lazy='dynamic',
                                        foreign_keys='Book.book_author_name')
    book_author_lastname = db.relationship('Book', backref='lastname', lazy='dynamic',
                                            foreign_keys='Book.book_author_lastname')

    def json_dump(self):
        return dict(id=self.id, name=self.name, lastname=self.lastname)

    def __repr__(self):
        return '<Author %r>' % (self.name)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(300), nullable=False)
    book_type = db.Column(db.String(100), db.ForeignKey('book_type.type'), nullable=False)
    book_genre = db.Column(db.String(100), db.ForeignKey('book_genre.genre'), nullable=False)
    book_author_name = db.Column(db.String(150), db.ForeignKey('author.name'), nullable=False)
    book_author_lastname = db.Column(db.String(150), db.ForeignKey('author.lastname'), nullable=False)
    status = db.Column(db.Integer)
    statusperson = db.Column(db.String(150))

    def json_dump(self):
        return dict(id=self.id, book_name=self.book_name, book_type=self.book_type,
                    book_genre=self.book_genre, book_author_name=self.book_author_name,
                    book_author_lastname=self.book_author_lastname)

    def __repr__(self):
        return '<Name %r>' % (self.book_name)