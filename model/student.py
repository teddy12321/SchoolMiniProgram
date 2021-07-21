from data import db
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    stuNo = db.Column(db.String(100),nullable = False)
    gender = db.Column(db.Integer,nullable=False)
    daysLate = db.Column(db.Integer, nullable = False)
    daysAbsent = db.Column(db.Integer, nullable = False)
    memo = db.Column(db.String(100),nullable = True)
    avatar = db.Column(db.String(5000),nullable = True)
    engName = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable = False)
    pinyin =  db.Column(db.String(100), nullable=False)
    #外键
    classId = db.Column(db.Integer,db.ForeignKey("class.id"))
    classs = db.relationship("Classs",backref=db.backref("students"))


    scheduleId = db.Column(db.Integer,db.ForeignKey("schedule.id"))
    schedule = db.relationship("Schedule",backref=db.backref("students"))

    def __init__(self,name,stuNo,year,schedule, classs,gender, daysLate, daysAbsent, memo, avatar, engName, pinyin):
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
        self.year = year
        self.pinyin = pinyin

    def __str__(self):
        return '姓名:%s' % (self.name)

    def getSchedule(self):
        type = self.scheduleId
        return type

    def getName(self):
        return self.name

    def getstuNo(self):
        return  self.stuNo

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