#!/usr/bin/python3
# Models for Series MicroService
"""
 Author: Daniel Córdova A.
"""

from app import db


class SeriesType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    genres = db.relationship('SeriesGenre', backref='gender_type', lazy='dynamic')
    series = db.relationship('Series', backref='series_type_name', lazy='dynamic')

    def json_dump(self):
        return dict(
            id=self.id,
            type_name=self.type_name
        )

    def __repr__(self):
        return '<SeriesType %r>' % self.type_name


class SeriesGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('series_type.id'), nullable=False)
    genre = db.Column(db.String(100), index=True, nullable=False)
    series = db.relationship('Series', backref='gender', lazy='dynamic')

    def json_dump(self):
        return dict(
            id=self.id,
            genre=self.genre,
            type_id=self.type_id
        )

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
            series_type=self.type_id,
            genre_id=self.genre_id
        )

    def __repr__(self):
        return '<Name %r>' % self.name
