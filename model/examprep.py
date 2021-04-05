from data import db
import json
class ExamPrep(db.Model):
    __tablename__ = 'examprep'
    id = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.String(1000),nullable = False)

    def __init__(self,data):
        self.data = json.dumps(data)

    def __str__(self):
        return 'data:%s' % (self.data)

    def getDic(self):
        return json.loads(self.data)