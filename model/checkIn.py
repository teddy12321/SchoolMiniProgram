from data import db
class CheckIn(db.Model):
    __tablename__ = 'checkin'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100),nullable = False)
    time = db.Column(db.String(100), nullable=False)

    stuid = db.Column(db.Integer,db.ForeignKey("student.id"))
    student = db.relationship("Student",backref=db.backref("checkins"))


    def __init__(self, date, time, stu):
        self.date = date
        self.time = time
        self.student = stu



    def __str__(self):
        return 'id' % (self.id)
