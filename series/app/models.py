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
        return dict(id=self.id, type_name=self.type_name)

    def __repr__(self):
        return '<SeriesType %r>' % self.type_name


class SeriesGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), index=True, nullable=False)
    type_name = db.Column(db.String(100), db.ForeignKey('series_type.type_name'), nullable=False)
    series = db.relationship('Series', backref='gender', lazy='dynamic')

    def json_dump(self):
        return dict(id=self.id, genre=self.genre, type_name=self.type_name)

    def __repr__(self):
        return '<SeriesGenre %r>' % self.genre


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series_name = db.Column(db.String(300), nullable=False)
    series_type = db.Column(db.String(100), db.ForeignKey('series_type.type_name'), nullable=False)
    series_genre = db.Column(db.String(100), db.ForeignKey('series_genre.genre'), nullable=False)

    def json_dump(self):
        return dict(id=self.id, series_name=self.series_name, series_type=self.series_type,
                    series_genre=self.series_genre)

    def __repr__(self):
        return '<Name %r>' % self.series_name