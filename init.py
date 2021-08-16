from data import db
from model.classs import Classs
from model.student import Student
from model.exam import Exam
from model.absent import Absent
from model.schedule import Schedule
from model.examprep import ExamPrep
from model.acti import Acti
from model.user import User
from model.admin import Admin
from model.checkIn import CheckIn
from model.scheduleTemplate import ScheduleTemplate
from model.language import Language
db.create_all()

# openid1 = User('qwertyuiop', '201901003')
# acti1 = Acti('q', 'w', 'e', 'r')
#
# class1 = Classs('高一1班')
#class2 = Classs('高一1班')
# # class3 = Classs('高三1班')
# # db.session.add(class1)
# # db.session.add(class3)
#s1 = ScheduleTemplate('A',class2,\
#                      '高一语文','高一语文','Intro to Writ \n Room 204','ELC1|AP Seminar\nRoom 203','ELC1|AP Seminar\nRoom 203','Pre-Cal\nRoom 208','高一地理','Counseling','高一体育',\
 #                     '高一物理','TOEFL\nRoom 203','Pre-Phy\nroom 212','Pre-Phy\nRoom 212','高一化学','ELC1|AP Seminar\nRoom 203','班会','大扫除','大扫除',\
 #                    '高一物理','高一数学','ELC1|AP Seminar\nRoom 203','Pre-Cal\nRoom 208','高一美术/音乐','Intro to Writ \n Room 204','Intro to Writ \n Room 204','高一政治','高一体育',\
 #                  'Pre-Cal\nRoom 208','高一化学','Intro to Writ \n Room 204','Pre-Phy\nroom 212','Pre-Phy\nroom 212','高一语文','ELC1|AP Seminar\nRoom 203','Self Study','高一历史',\
 #                     'TOEFL\nRoom 203','Pre-Cal\nRoom 208','Self Study','Intro to Writ \n Room 204','ELC1|AP Seminar\nRoom 203','Pre-Phy\nRoom 212','高一数学','二课堂','二课堂')
#s2 = ScheduleTemplate('B',class2,\
  #           '高一语文','高一语文','Pre-Phy\nroom 212','Pre-Cal\nRoom 208','TOEFL\nRoom 203','ELC C2','高一地理','Counseling','高一体育',\
   #         '高一物理','ELC C2','Intro to Writ \n Room 204','Intro to Writ \n Room 204','高一化学','Pre-Cal\nRoom 208','班会','大扫除','大扫除',\
    #        '高一物理','高一数学','Pre-Cal\nRoom 208','ELC C2','高一美术/音乐','Pre-Phy\nroom 212','Pre-Phy\nroom 212','高一政治','高一体育',\
     #       'ELC C2','高一化学','Pre-Phy\nroom 212','Intro to Writ \n Room 204','Intro to Writ \n Room 204','高一语文','Pre-Cal\nRoom 208','Self Study','高一历史',\
      #      'ELC C2','ELC C2','Self Study','Pre-Phy\nroom 212','TOEFL\nRoom 203','Intro to Writ \n Room 204','高一数学','二课堂','二课堂')

#ss = Schedule('高一语文','高一语文','Intro to Writ \n Room 204','ELC1|AP Seminar\nRoom 203','ELC1|AP Seminar\nRoom 203','Pre-Cal\nRoom 208','高一地理','Counseling','高一体育',\
       #               '高一物理','TOEFL\nRoom 203','Pre-Phy\nroom 212','Pre-Phy\nRoom 212','高一化学','ELC1|AP Seminar\nRoom 203','班会','大扫除','大扫除',\
        #             '高一物理','高一数学','ELC1|AP Seminar\nRoom 203','Pre-Cal\nRoom 208','高一美术/音乐','Intro to Writ \n Room 204','Intro to Writ \n Room 204','高一政治','高一体育',\
          #         'Pre-Cal\nRoom 208','高一化学','Intro to Writ \n Room 204','Pre-Phy\nroom 212','Pre-Phy\nroom 212','高一语文','ELC1|AP Seminar\nRoom 203','Self Study','高一历史',\
           #           'TOEFL\nRoom 203','Pre-Cal\nRoom 208','Self Study','Intro to Writ \n Room 204','ELC1|AP Seminar\nRoom 203','Pre-Phy\nRoom 212','高一数学','二课堂','二课堂')

#chenrun = Student('陈润','201901003',1,ss,class2, 0, 1,2,'get to work!', 'trdfhg', 'Ben', 'Chen Run')
# chenyufan = Student('陈禹帆','201901007',class2, s1,0, 3,5,'wake up!', 'asfhg', 'Peter')
# zhaojinxing = Student('赵金星','201901004',class2, s2, 0, 0,0,'!', 'rgdfhg', 'Tony')
# euclid = Exam('Euclid', '2020.4.8', 'Math')
# comc = Exam('COMC', '2020.11', 'Math')
# bpho = Exam('BPHO', '2020.12', 'Physics')
# examprepList = ExamPrep([{"AP": [
#     {"name": "Calc-BC", "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
#     {"name": "Phys-C", "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
#     {"name": "Chem", "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]}]},
#                 {"Contests": [{"name": "Euclid",
#                                "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
#                               {"name": "COMC",
#                                "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
#                               {"name": "BPHO",
#                                "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]}]}])
# db.session.add(chenrun)
# db.session.add(chenyufan)
# db.session.add(zhaojinxing)
# db.session.add(examprepList)
# db.session.add(euclid)
# db.session.add(comc)
# db.session.add(bpho)
# db.session.add(acti1)
# db.session.add(openid1)
# checkIn1 = CheckIn('2021.6.1','07:58', Student.query.filter(Student.stuNo == '201901003').first())
# db.session.add(abs1)
# admin = Admin('dfgu')
# db.session.add(admin)

db.session.commit()
