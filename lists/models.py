from django.db import models
from django.db import models
class Userinfo(models.Model):
    #objects = None
    objects = None
    name = models.TextField(max_length=200, blank=True)
    #password = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.name
class Term1(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)

class Term2(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term3(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term4(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term5(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)

class Term6(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term7(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term8(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)