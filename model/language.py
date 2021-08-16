from data import db
class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer,primary_key = True)
    openid = db.Column(db.String(100),nullable = False)
    name = db.Column(db.String(100),nullable = False)

    def __init__(self,name, openid):
        self.name = name
        self.openid = openid
    def __str__(self):
        return '名称:%s' % (self.name)

    def getName(self):
        return  self.name

    def getDic(self):
        language = {"name": self.name,
                    "openid": self.openid
                    }
        return language