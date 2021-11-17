from django.db import models

# Create your models here.
from django.urls import reverse


class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    disease_code = models.CharField(max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)

    def __str__(self):
        return '{}: {}'.format(self.id, self.disease_code)

    def to_json(self):
        return{
            'id': self.id,
            'disease_code': self.disease_code,
            'pathogen': self.pathogen,
            'description': self.description
        }

    def get_UpdateUrl(self):
        return reverse('dis_update', kwargs={'pk': self.pk})

    def get_DeleteUrl(self):
        return reverse('dis_delete', kwargs={'pk': self.pk})

class MainTable(models.Model):
    id = models.AutoField(primary_key=True)
    disease_type = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return '{}: {}'.format(self.id, self.disease_type)

    def to_json(self):
        return{
            'id': self.id,
            'disease_type': self.disease_type,
            'country': self.country
        }

class Discover(models.Model):
    id = models.AutoField(primary_key=True)
    d_cname = models.ForeignKey(MainTable, on_delete=models.CASCADE)
    d_disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    first_enc_date = models.DateField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.d_cname)

    def to_json(self):
        return{
            'id': self.id,
            'cname': self.d_cname,
            'disease_code': self.d_disease_code,
            'first_enc_date': self.first_enc_date
        }

class Duser(models.Model):

    email = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    u_cname = models.ForeignKey(MainTable, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.email)

    def to_json(self):
        return{
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'surname': self.surname,
            'salary': self.salary,
            'phone': self.phone,
            'cname': self.u_cname
        }

class PublicServant(models.Model):
    p_email = models.ForeignKey(Duser, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return '{}: {}'.format(self.id, self.p_email)

    def to_json(self):
        return{
            'id': self.id,
            'email': self.p_email,
            'department': self.department
        }

class Doctor(models.Model):
    d_email = models.ForeignKey(Duser, on_delete=models.CASCADE)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return '{}: {}'.format(self.id, self.d_email)

    def to_json(self):
        return{
            'id': self.id,
            'email': self.d_email,
            'degree': self.degree
        }

class Specialize(models.Model):
    #id = models.ForeignKey(MainTable, on_delete=models.CASCADE, related_name='disease_type')
    s_email = models.ForeignKey(Duser, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.s_email)

    def to_json(self):
        return{
            'id': self.id,
            'email': self.s_email
        }

class Record(models.Model):
    r_email = models.ForeignKey(PublicServant, on_delete=models.CASCADE)
    r_cname = models.ForeignKey(MainTable, on_delete=models.CASCADE)
    r_disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.r_disease_code)

    def to_json(self):
        return{
            'id': self.id,
            'email': self.r_email,
            'cname': self.r_cname,
            'disease_code': self.r_disease_code,
            'total_deaths': self.total_deaths,
            'total_patients': self.total_patients
        }
