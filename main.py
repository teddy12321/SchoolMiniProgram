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
from model.user import User

@app.route('/acti')
def recentActi():
   actis = Acti.query.all()
   res = []
   for acti in actis:
      res.append(acti.getDic())
   print(res)
   return jsonify(res)

@app.route('/schedule/<stuno>')
def classSchedule(stuno):
   stu = Student.query.filter(Student.stuNo == stuno).first()
   schedule = Schedule.query.filter(Schedule.id == stu.getType()).first()
   return jsonify(schedule.construct())

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

@app.route('/checkid', methods = ['POST'])
def checkId():
   req = request.json
   openid = req.get('openid')
   print(openid)
   stuno = ""
   stu = User.query.filter(User.openid==openid).first()
   if(stu != None):
      if(stu.stuNo != None):
         stuno = stu.stuNo
   else:
      newusr = User(openid, None)
      db.session.add(newusr)
      db.session.commit()

   return jsonify({'res':True,
                   'stuno': stuno
                   })

nameList = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

@app.route('/checkdayschedule', methods = ['POST'])
def checkDaySchedule():
   schList = []
   req = request.json
   stuNo = req.get('stu')
   pos = req.get('day')
   stu = Student.query.filter(Student.stuNo==stuNo).first()
   type = stu.getType()
   schedule = Schedule.query.filter(Schedule.id == type).first()
   for i in range(1,10):
      schList.append(getattr(schedule,nameList[pos]+str(i),''))

   return jsonify({'res':True,
                   'data': schList
                   })

@app.route('/postid', methods = ['POST'])
def postId():
   req = request.json
   print(req)
   openid = req.get('openid')
   stuno = req.get('stuno')
   name = req.get('name')
   print(stuno)
   print(name)
   stu = Student.query.filter(Student.stuNo == stuno).filter(Student.name == name).first()
   if(stu != None):
      usr = User.query.filter(User.openid == openid).first()
      if(usr != None):
         usr.stuNo = stuno
         db.session.commit()
         return jsonify({'res': True})
      else:
         newusr = User(openid, stuno)
         db.session.add(newusr)
         db.session.commit()
         return jsonify({'res': True})
   return jsonify({'res': False})


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000)