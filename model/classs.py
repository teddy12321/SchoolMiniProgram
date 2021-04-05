from data import db
class Classs(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    teacher = db.Column(db.String(100),nullable = False)
    teacherPhone = db.Column(db.String(100),nullable = False)
    state = db.Column(db.Integer,nullable=False)

    def __init__(self,name,teacher="",teacherPhone="",state=0):
        self.name = name
        self.teacher = teacher
        self.teacherPhone = teacherPhone
        self.state = state
    def __str__(self):
        return '班级名: %s 状态: %s' % (self.name,self.state)

    def getDic(self):
        return {
            "classname":self.name,
            "id": self.id
        }