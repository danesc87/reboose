from app import db

class BookType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), index=True, unique=True)
    genders = db.relationship('BookGenre', backref='types', lazy='dynamic')

    def __repr__(self):
        return '<BookType %r>' % (self.type)

class BookGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), index=True, unique=True)
    type = db.Column(db.Integer, db.ForeignKey('book_type.id'))
    books = db.relationship('Books', backref='gender', lazy='dynamic')

    def __repr__(self):
        return '<BookGenre %r>' % (self.genre)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)
    books = db.relationship('Books', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Author %r>' % (self.name)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(300))
    # book_type = db.Column(db.String(100), db.ForeignKey('book_type.type'))
    book_genre = db.Column(db.Integer, db.ForeignKey('book_genre.id'))
    book_author = db.Column(db.String(150), db.ForeignKey('author.name'))
    status = db.Column(db.Integer)
    statusperson = db.Column(db.String(150))

    def __repr__(self):
        return '<Name %r>' % (self.book_name)