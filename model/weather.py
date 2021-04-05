from data import db
class Weather(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Integer,primary_key = True)
    weather = db.Column(db.String(100),nullable = False)
    date = db.Column(db.String(100),nullable = False)
    pm25 = db.Column(db.Float,nullable=False)
    def __init__(self,weather, date, pm25):
        self.weather = weather
        self.date = date
        self.pm25 = pm25

    def __str__(self):
        return '名称:%s' % (self.name)

    def getDic(self):
        exam = {"name": self.name,
                "date": self.date,
                "summary": self.summary,
                "img": self.img
                    }