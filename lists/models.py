from django.db import models
from django.db import models


class Userinfo(models.Model):
    # new repo for incomplete

    # create model name as TextField to collect user name
    name = models.TextField(max_length=200, blank=True)

    # seperate each terms' model as ManyToManyField to collect user data in each term


    # create GPA model as ManyToManyField to collect user GPA
    gpa = models.ManyToManyField('GPA')

    term_All = models.ManyToManyField('Term')

    # password = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.name


'''Now in each term (from 1 to 8) we will collect as CharField with max_length=255
1. subject name
2. unit 
3. grade (F-A)
4. GPA
'''
class Term(models.Model):
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)

# for GPA we will collect GPA from each term (1-8)
class GPA(models.Model):
    # สร้างโมเดลสำหรับเก็บ GPA ของ user ในแต่ละเทอมโดยเป็น CharField และมีความยาวสูงสุด 255 ตัวอักษร

    GPA_1 = models.CharField(max_length=255)
    GPA_2 = models.CharField(max_length=255)
    GPA_3 = models.CharField(max_length=255)
    GPA_4 = models.CharField(max_length=255)
    GPA_5 = models.CharField(max_length=255)
    GPA_6 = models.CharField(max_length=255)
    GPA_7 = models.CharField(max_length=255)
    GPA_8 = models.CharField(max_length=255)
