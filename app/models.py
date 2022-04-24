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
    id = db.Column(db.Integer, primary_key = True)
    
    hiveid = db.Column(db.String(16), db.ForeignKey('user.hiveid'))

    temp = db.Column(db.String(255))
    hum = db.Column(db.String(255))
    weight = db.Column(db.String(255))
    energy = db.Column(db.String(255))
    
    timestamp = db.Column(db.DateTime)


    def __repr__(self) -> str:
        return f'Hive {self.hiveid}'