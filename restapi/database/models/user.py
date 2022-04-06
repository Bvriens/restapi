from ..db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from .movie import Movie

class User(db.Document):
    name = db.StringField(required=True, unique=False)
    email = db.EmailField(required=True, unique=False)
    password = db.StringField(required=True, min_length=6)
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))
 
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Movie, 'added_by', db.CASCADE)