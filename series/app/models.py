#!/usr/bin/python3
# Models for Series MicroService
"""
 Author: Daniel Córdova A.
"""

from app import db


class SeriesType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), index=True, unique=True, nullable=False)
    genres = db.relationship('SeriesGenre', backref='gender_type', lazy='dynamic')
    series = db.relationship('Series', backref='series_type_name', lazy='dynamic')

    def json_dump(self):
        return dict(
            id=self.id,
            type=self.type
        )

    @staticmethod
    def fields():
        return ['type']

    def __repr__(self):
        return '<SeriesType %r>' % self.type


class SeriesGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('series_type.id'), nullable=False)
    genre = db.Column(db.String(100), index=True, nullable=False)
    series = db.relationship('Series', backref='series_genre', lazy='dynamic')

    def json_dump(self):
        return dict(
            id=self.id,
            genre=self.genre,
            type=self.gender_type.type
        )

    @staticmethod
    def fields():
        return ['type_id', 'genre']

    def __repr__(self):
        return '<SeriesGenre %r>' % self.genre


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('series_type.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('series_genre.id'), nullable=False)
    name = db.Column(db.String(300), nullable=False)

    def json_dump(self):
        return dict(
            id=self.id,
            name=self.name,
            type=self.series_type_name.type,
            genre=self.series_genre.genre
        )

    @staticmethod
    def fields():
        return ['type_id', 'genre_id', 'name']

    def __repr__(self):
        return '<Name %r>' % self.name
