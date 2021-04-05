from data import db
class Acti(db.Model):
    __tablename__ = 'acti'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    date = db.Column(db.String(100),nullable = False)
    summary = db.Column(db.String(100),nullable=False)
    img = db.Column(db.String(5000),nullable=False)
    def __init__(self,name, date, summery, img):
        self.name = name
        self.date = date
        self.summary = summery
        self.img = img

    def __str__(self):
        return '名称:%s' % (self.name)

    def getDic(self):
        exam = {"name": self.name,
                "date": self.date,
                "summary": self.summary,
                "img": self.img
                    }