from data import db
class DelAbsent(db.Model):
    __tablename__ = 'delAbsent'
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)

    def __init__(self, period, date):
        self.period = period
        self.date = date


    def __str__(self):
        return '名称:%s' % (self.d1)

    def getDic(self):
        delabsent = {"period": self.period,
                "date": self.date,
                }