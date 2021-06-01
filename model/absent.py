from data import db
class Absent(db.Model):
    __tablename__ = 'absent'
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(100), nullable=False)
    isCompleted = db.Column(db.Boolean, nullable=False)
    stuid = db.Column(db.Integer,db.ForeignKey("student.id"))
    Student = db.relationship("Student",backref=db.backref("absents"))


    def __init__(self, period, date, stu):
        self.period = period
        self.date = date
        self.Student = stu
        self.isCompleted = False


    def __str__(self):
        return '名称:%s' % (self.d1)

    def getDic(self):
        absent = {"period": self.period,
                "date": self.date,
                }