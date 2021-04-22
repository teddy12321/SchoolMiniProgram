from flask import  jsonify
from data import app

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

@app.route('/examprep')
def examprep():
   prep1 = ExamPrep.query.filter(ExamPrep.id == 1).first()
   return jsonify(prep1.getDic())


@app.route('/weather')
def weather():
   tdweather = {"date": " ", "weather": " ", "PM2.5": " "}
   return jsonify(tdweather)

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


@app.route('/applyabsent')
def absent():
   absentData = Absent.query.filter(Absent.id == 1).first()
   return jsonify(absentData)


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000)