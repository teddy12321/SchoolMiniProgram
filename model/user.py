from data import db
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    openid = db.Column(db.String(100),nullable = False)
    stuNo = db.Column(db.String(100))

    def __init__(self, opid, code):
        self.openid = opid
        self.stuNo = code


