from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author}"

# Create application context
with app.app_context():
    # Create all tables
    db.create_all()