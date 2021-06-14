from data import db
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(100),nullable = False)

    def __init__(self, openid):
        self.openid = openid



    def __str__(self):
        return 'openid' % (self.openid)
