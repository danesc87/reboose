#!/usr/bin/python3
# Models for Series Microservice
'''
 Author: Daniel Córdova A.
'''

from app import db

class SerieType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), index=True, unique=True, nullable=False)
    genres = db.relationship('SerieGenre', backref='gender_type', lazy='dynamic')
    book = db.relationship('Serie', backref='type', lazy='dynamic')

    def json_dump(self):
        return dict(id=self.id, type=self.type)

    def __repr__(self):
        return '<SerieType %r>' % (self.type)

class SerieGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), index=True, nullable=False)
    type = db.Column(db.String(100), db.ForeignKey('serie_type.type'), nullable=False)
    book = db.relationship('Serie', backref='gender', lazy='dynamic')

    def json_dump(self):
        return dict(id=self.id, genre=self.genre, type=self.type)

    def __repr__(self):
        return '<SerieGenre %r>' % (self.genre)

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serie_name = db.Column(db.String(300), nullable=False)
    serie_type = db.Column(db.String(100), db.ForeignKey('serie_type.type'), nullable=False)
    serie_genre = db.Column(db.String(100), db.ForeignKey('serie_genre.genre'), nullable=False)

    def json_dump(self):
        return dict(id=self.id, serie_name=self.serie_name, serie_type=self.serie_type,
                    serie_genre=self.serie_genre)

    def __repr__(self):
        return '<Name %r>' % (self.book_name)