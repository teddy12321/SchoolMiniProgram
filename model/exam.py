from data import db
class Exam(db.Model):
    __tablename__ = 'exam'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    date = db.Column(db.String(100),nullable = False)
    subject = db.Column(db.String(100),nullable=False)

    def __init__(self,name, date, subject):
        self.name = name
        self.date = date
        self.subject = subject

    def __str__(self):
        return '名称:%s' % (self.name)

    def getDic(self):
        exam = {"name": self.name,
                "date": self.date,
                "subject": self.subject,
                    }
        return  exam