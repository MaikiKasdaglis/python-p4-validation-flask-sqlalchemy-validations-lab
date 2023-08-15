from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Name cannot be empty')
        return name
    phone_number = db.Column(db.String(10))
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10: 
            raise ValueError('must be 10 digits, bro')
        return phone_number

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError('Content must be at least 250 characters long')
        return content
    category = db.Column(db.String)
    @validates('category')
    def validate_category(self, key, category):
        if category == "Fiction" or category == "Non-Fiction":
            return category
        else:
            raise ValueError('must be Fiction of Non-Fiction. there is no grey area.')
    summary = db.Column(db.String)
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError('Summary length cannot exceed 250 characters')
        return summary
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
