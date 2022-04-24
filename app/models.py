from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    username = db.Column(db.String(64), index = True,
     unique = True)
    
    email = db.Column(db.String(120), index = True,
     unique = True)
    
    password = db.Column(db.String(255), index = True,
     unique = True)

    hiveid = db.Column(db.String(16), index = True,
     unique = True)
    
    def __repr__(self) -> str:
        return f'<User {self.username}>'

class hive(db.Model):
    ...