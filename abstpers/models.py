from django.db import models
from datetime import date


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        return date.today().year - self.birth_date


class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField()
    work_experience = models.DateField()


class Client(AbstractPerson):
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=14)


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()


class WorkProject(models.Model):
    project_name = models.CharField(max_length=20)


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workproject = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True)


class Passport(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    inn = models.CharField(max_length=14)
    id_card = models.CharField(max_length=6)

    def get_gender(self):
        inn = int(str(self.inn)[0])
        if inn == 1:
            return 'Male'
        elif inn == 2:
            return 'FeMale'
        else:
            return 'False'

