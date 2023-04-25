from django.db import models

class Course(models.Model):
    name_course = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    student = models.CharField(max_length=30)
    mentor = models.CharField(max_length=30)

    def __str__(self):
        return self.name_course


class Student(models.Model):
    fio = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.fio


class Mentors(models.Model):
    fio_mentr = models.CharField(max_length=50)
    expenience = models.CharField(max_length=10)

    def __str__(self):
        return self.fio_mentr



