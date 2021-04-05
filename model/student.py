from data import db
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    stuNo = db.Column(db.String(100),nullable = False)
    gender = db.Column(db.Integer,nullable=False)
    daysLate = db.Column(db.Integer, nullable = False)
    daysAbsent = db.Column(db.Integer, nullable = False)
    memo = db.Column(db.String(100),nullable = False)
    avatar = db.Column(db.String(5000),nullable = False)
    engName = db.Column(db.String(100), nullable=False)
    #外键
    classId = db.Column(db.Integer,db.ForeignKey("class.id"))
    classs = db.relationship("Classs",backref=db.backref("students"))


    scheduleId = db.Column(db.Integer,db.ForeignKey("schedule.id"))
    schedule = db.relationship("Schedule",backref=db.backref("students"))

    def __init__(self,name,stuNo, classs= None,schedule = None,gender=0, daysLate = 0, daysAbsent = 0, memo = " ", avatar = " ", engName = " "):
        self.name = name
        self.classs = classs
        self.stuNo = stuNo
        self.gender = gender
        self.daysLate = daysLate
        self.daysAbsent = daysAbsent
        self.memo = memo
        self.schedule = schedule
        self.avatar = avatar
        self.engName = engName
    def __str__(self):
        return '姓名:%s' % (self.name)

    def getDic(self):
        stuinfos = {"name": self.name,
                    "code": self.stuNo,
                    "dayslate": self.daysLate,
                    "daysabsent": self.daysAbsent,
                    "avatar": self.avatar,
                    "memo": self.memo,
                    "class": self.classs.getDic(),
                    "Schedule": self.schedule.getDic(),
                    "engName": self.engName
                    }
        return stuinfos