
(venv) C:\Users\Acer\Desktop\my_projects\asdf>python manage.py shell
>>> from abstpers.models import *

a = Employee.objects.create(name='Alex', birth_date='2000-1-1', position='develop', salary=10000, work_experience='2023-1-1')

a2 = Employee.objects.create(name='Two', birth_date='2002-2-2', position ='JS', salary=20000, work_experience='2022-2-2')
a3 = Employee.objects.create(name='Three', birth_date='2003-3-3', position ='PM', salary=30000, work_experience='2021-3-3')
a4 = Employee.objects.create(name='Four', birth_date='2004-4-4', position ='Python', salary=40000, work_experience='2020-4-4')
p1 = Passport.objects.create(employee=a, inn='1243', id_card='124124')
p2 = Passport.objects.create(employee=a2, inn='23555', id_card='23533')
p3 = Passport.objects.create(employee=a3, inn='124214', id_card='23533')
p4 = Passport.objects.create(employee=a4, inn='2324634', id_card='21235')
Passport.objects.filter(id=3).delete()
Employee.objects.filter(id=3).delete()
wp = WorkProject.objects.create(project_name='gg_wp')
membr = Membership(employee=a, workproject=wp)
membr = Membership(employee=a2, workproject=wp)
membr = Membership(employee=a3, workproject=wp)

c1 = Client.objects.create(name='Cone', birth_date='2004-4-4', address='Bish', phone_number='21213213')
c2 = Client.objects.create(name='Ctwo', birth_date='2005-5-5', address='Osh', phone_number='56765765')
c3 = Client.objects.create(name='Cthree', birth_date='2006-6-6', address='Naryn', phone_number='45645645')

Client.objects.filter(id=2).delete()
Employee.objects.all()
Passport.objects.all()
WorkProject.objects.all()
Client.objects.all()
VIPClient.objects.all()
