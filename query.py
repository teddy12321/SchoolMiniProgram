
from model.exam import Exam
from model.schedule import Schedule
# stu1 = Student.query.filter_by(id=1).first()
# all_class = Student.query.filter(Student.stuNo > 10500).order_by(Student.name.desc()).all()
#
# print(stu1)
#
# for classs in all_class:
#     print(classs.name,classs.state,classs.stuNo)

www = Schedule.query.filter(Exam.id==1).first()
print(www)