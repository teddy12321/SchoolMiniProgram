from flask import  jsonify,request
from pip._vendor import requests

from data import app
from data import db
# @app.route('/')
# def root():
#    return 'root'
#
# @app.route('/abc')
# def abc():
#    testDic = {'res':True,'msg':'xxxx','data':[1,2,'aa']}
#    testList = []
#    for i in range(100):
#       testList.append(testDic)
#    return jsonify(testList)
#
from model.absent import Absent
from model.classs import Classs
from model.student import Student
from model.exam import Exam
from model.examprep import ExamPrep
from model.schedule import Schedule
from model.acti import Acti
from model.weather import Weather
from model.delAbsent import DelAbsent


@app.route('/acti/<date>')
def recentActi(date):
   actisList = [{"date": "2020.10.31", "name": "Halloween", "summary": " ", "img:": ""},
                {"date": "2020.12.24", "name": "Christmas", "summary": " ", "img:": ""},
                {"date": "2021.3.14", "name": "Pi-day", "summary": " ", "img:": ""}]
   return jsonify(actisList)

@app.route('/schedule')
def classSchedule():
   Monday = ["Chi", "ELC", "ELL", "Cap", "Calc-BC", "Chem", "PBL", "PE", "Self-study"]
   Tuesday = ["Chi", "ELC", "ELL", "Cap", "Calc-BC", "Chem", "PBL", "PE", "Self-study"]
   Wednesday = ["Chi", "ELC", "ELL", "Cap", "Calc-BC", "Chem", "PBL", "PE", "Self-study"]
   Thursday = ["Chi", "ELC", "ELL", "Cap", "Calc-BC", "Chem", "PBL", "PE", "Self-study"]
   Friday = ["Chi", "ELC", "ELL", "Cap", "Calc-BC", "Chem", "PBL", "PE", "Self-study"]
   classList = [Monday, Tuesday, Wednesday, Thursday, Friday]
   return jsonify(classList)

@app.route('/exams/<name>')
def exams(name):
   exam1 = Exam.query.filter(Exam.name == name).first()
   print(exam1)
   return jsonify(exam1.getDic())

@app.route('/exams')
def examsall():
   exam1 = Exam.query.all()
   res = []
   for exam in exam1:
      res.append(exam.getDic())
   print(exam1)
   return jsonify(res)

@app.route('/examprep')
def examprep():
   prep1 = ExamPrep.query.filter(ExamPrep.id == 1).first()
   return jsonify(prep1.getDic())


@app.route('/weather')
def weather():
   url = f'http://wthrcdn.etouch.cn/weather_mini?citykey=101030100'
   res = requests.get(url)
   # tdweather = {"date": " ", "weather": " ", "PM2.5": " "}
   return jsonify(res.json())

# @app.route('/login')
# def login():
#    usrname = request.args['usrname']
#    pwd = request.args['pwd']
#    return 0

@app.route('/stuinfo/<stuno>')
def stuinfo(stuno):
   stu1 = Student.query.filter(Student.stuNo==stuno).first()
   print(stu1)
   return jsonify(stu1.getDic())


@app.route('/applyabsent',methods=['POST'])
def absent():
   req = request.json
   periods = req.get('periods')
   date = req.get('date')
   print(date)
   for period in periods:
      print(period)
      absent = Absent(period,date)
      db.session.add(absent)
   db.session.commit()
   return jsonify({'res':True})




if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000)