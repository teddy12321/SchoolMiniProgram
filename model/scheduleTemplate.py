from data import db
class ScheduleTemplate(db.Model):
    __tablename__ = 'scheduletemplate'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), nullable=False)
    mon1 = db.Column(db.String(100), nullable=False)
    mon2 = db.Column(db.String(100), nullable=False)
    mon3 = db.Column(db.String(100), nullable=False)
    mon4 = db.Column(db.String(100), nullable=False)
    mon5 = db.Column(db.String(100), nullable=False)
    mon6 = db.Column(db.String(100), nullable=False)
    mon7 = db.Column(db.String(100), nullable=False)
    mon8 = db.Column(db.String(100), nullable=False)
    mon9 = db.Column(db.String(100), nullable=False)
    tue1 = db.Column(db.String(100), nullable=False)
    tue2 = db.Column(db.String(100), nullable=False)
    tue3 = db.Column(db.String(100), nullable=False)
    tue4 = db.Column(db.String(100), nullable=False)
    tue5 = db.Column(db.String(100), nullable=False)
    tue6 = db.Column(db.String(100), nullable=False)
    tue7 = db.Column(db.String(100), nullable=False)
    tue8 = db.Column(db.String(100), nullable=False)
    tue9 = db.Column(db.String(100), nullable=False)
    wed1 = db.Column(db.String(100), nullable=False)
    wed2 = db.Column(db.String(100), nullable=False)
    wed3 = db.Column(db.String(100), nullable=False)
    wed4 = db.Column(db.String(100), nullable=False)
    wed5 = db.Column(db.String(100), nullable=False)
    wed6 = db.Column(db.String(100), nullable=False)
    wed7 = db.Column(db.String(100), nullable=False)
    wed8 = db.Column(db.String(100), nullable=False)
    wed9 = db.Column(db.String(100), nullable=False)
    thu1 = db.Column(db.String(100), nullable=False)
    thu2 = db.Column(db.String(100), nullable=False)
    thu3 = db.Column(db.String(100), nullable=False)
    thu4 = db.Column(db.String(100), nullable=False)
    thu5 = db.Column(db.String(100), nullable=False)
    thu6 = db.Column(db.String(100), nullable=False)
    thu7 = db.Column(db.String(100), nullable=False)
    thu8 = db.Column(db.String(100), nullable=False)
    thu9 = db.Column(db.String(100), nullable=False)
    fri1 = db.Column(db.String(100), nullable=False)
    fri2 = db.Column(db.String(100), nullable=False)
    fri3 = db.Column(db.String(100), nullable=False)
    fri4 = db.Column(db.String(100), nullable=False)
    fri5 = db.Column(db.String(100), nullable=False)
    fri6 = db.Column(db.String(100), nullable=False)
    fri7 = db.Column(db.String(100), nullable=False)
    fri8 = db.Column(db.String(100), nullable=False)
    fri9 = db.Column(db.String(100), nullable=False)

    classId = db.Column(db.Integer,db.ForeignKey("class.id"))
    classs = db.relationship("Classs",backref=db.backref("templates"))

    def construct(self):
        monday = [self.mon1, self.mon2, self.mon3, self.mon4, self.mon5, self.mon6, self.mon7, self.mon8, self.mon9]
        tuesday = [self.tue1, self.tue2, self.tue3, self.tue4,self.tue5,self.tue6,self.tue7,self.tue8,self.tue9]
        wednesday = [self.wed1, self.wed2, self.wed3, self.wed4, self.wed5, self.wed6, self.wed7, self.wed8, self.wed9]
        thursday = [self.thu1, self.thu2, self.thu3, self.thu4, self.thu5, self.thu6, self.thu7, self.thu8, self.thu9]
        friday = [self.fri1, self.fri2, self.fri3, self.fri4, self.fri5, self.fri6, self.fri7, self.fri8, self.fri9]
        overall = [monday, tuesday, wednesday,thursday, friday]
        return overall

    def makeData(self,datas):
        if(len(datas)<45):
            return False
        self.mon1 = datas[0]
        self.mon2 = datas[1]
        self.mon3 = datas[2]
        self.mon4 = datas[3]
        self.mon5 = datas[4]
        self.mon6 = datas[5]
        self.mon7 = datas[6]
        self.mon8 = datas[7]
        self.mon9 = datas[8]
        self.tue1 = datas[9]
        self.tue2 = datas[10]
        self.tue3 = datas[11]
        self.tue4 = datas[12]
        self.tue5 = datas[13]
        self.tue6 = datas[14]
        self.tue7 = datas[15]
        self.tue8 = datas[16]
        self.tue9 = datas[17]
        self.wed1 = datas[18]
        self.wed2 = datas[19]
        self.wed3 = datas[20]
        self.wed4 = datas[21]
        self.wed5 = datas[22]
        self.wed6 = datas[23]
        self.wed7 = datas[24]
        self.wed8 = datas[25]
        self.wed9 = datas[26]
        self.thu1 = datas[27]
        self.thu2 = datas[28]
        self.thu3 = datas[29]
        self.thu4 = datas[30]
        self.thu5 = datas[31]
        self.thu6 = datas[32]
        self.thu7 = datas[33]
        self.thu8 = datas[34]
        self.thu9 = datas[35]
        self.fri1 = datas[36]
        self.fri2 = datas[37]
        self.fri3 = datas[38]
        self.fri4 = datas[39]
        self.fri5 = datas[40]
        self.fri6 = datas[41]
        self.fri7 = datas[42]
        self.fri8 = datas[43]
        self.fri9 = datas[44]
        return True


    def __init__(self,name, cls, *overall):
        self.code = name
        self.classs = cls
        self.makeData(overall)

    def __str__(self):
        return ':%s' % (self.construct())

    # def getDic(self):
    #     scheduleinfo = {"name": self.name,
    #                 "code": self.stuNo,
    #                 "dayslate": self.daysLate,
    #                 "daysabsent": self.daysAbsent,
    #                 "avatar": self.avatar,
    #                 "memo": self.memo,
    #                 "class": self.classs.getDic(),
    #                 "Schedule": self.schedule.getDic(),
    #                 "engName": self.engName
    #                 }