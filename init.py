from data import db
from model.classs import Classs
from model.student import Student
from model.exam import Exam
from model.schedule import Schedule
from model.examprep import ExamPrep
db.create_all()

class1 = Classs('高一1班')
class2 = Classs('高二1班')
class3 = Classs('高三1班')
db.session.add(class1)
db.session.add(class3)
s1 = Schedule('1','1','1','1','1','1','1','1','1','2','2','2','2','2','2','2','2','2','3','3','3','3','3','3','3','3','3','4','4','4','4','4','4','4','4','4','5','5','5','5','5','5','5','5','5')
s2 = Schedule('2','1','1','1','1','1','1','1','1','2','2','2','2','2','2','2','2','2','3','3','3','3','3','3','3','3','3','4','4','4','4','4','4','4','4','4','5','5','5','5','5','5','5','5','5')
chenrun = Student('陈润','201901003',class2,s1, 0, 1,2,'get to work!', 'trdfhg', 'Ben')
chenyufan = Student('陈禹帆','201901007',class2, s1,0, 3,5,'wake up!', 'asfhg', 'Peter')
zhaojinxing = Student('赵金星','201901004',class2, s2, 0, 0,0,'!', 'rgdfhg', 'Tony')
euclid = Exam('Euclid', '2020.4.8', 'Math')
comc = Exam('COMC', '2020.11', 'Math')
bpho = Exam('BPHO', '2020.12', 'Physics')
examprepList = ExamPrep([{"AP": [
    {"name": "Calc-BC", "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
    {"name": "Phys-C", "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
    {"name": "Chem", "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]}]},
                {"Contests": [{"name": "Euclid",
                               "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
                              {"name": "COMC",
                               "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]},
                              {"name": "BPHO",
                               "file": [{"bkname": "Barron", "bkfile": " "}, {"bkname": "5 steps", "bkfile": " "}]}]}])
db.session.add(chenrun)
db.session.add(chenyufan)
db.session.add(zhaojinxing)
db.session.add(examprepList)

db.session.commit()

