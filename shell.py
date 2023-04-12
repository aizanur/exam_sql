from user.models import Language, Student, Mentor, Course
from datetime import datetime

python = Language(name='Python', month_to_learn=6)
python.save()

javascript = Language(name='JavaScript', month_to_learn=6)
javascript.save()

ux_ui = Language(name='UX-UI design', month_to_learn=2)
ux_ui.save()


aman = Student(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898', work_study_place='School №13', has_own_notebook=True, preferred_os='Windows')
aman.save()




phil = Student(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312', work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='Linux')
phil.save()


ilona = Mentor(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454', main_work=None, experience='2021-10-23 ')
ilona.save()

halil = Mentor(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876', main_work='University of Fort Collins', experience='2010-09-18')
halil.save()


python_course = Course(name='Python', language=python, date_started='2022-08-01', mentor=halil, student=aman)
python_course.save()

ux_ui_course = Course(name='UXUI design', language=ux_ui, date_started='2022-08-22', mentor=ilona, student=phil)
ux_ui_course.save()
