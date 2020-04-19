from django.db import models
from django.db import models


class Userinfo(models.Model):

    # new repo for incomplete
    
    # create model name as TextField to collect user name
    name = models.TextField(max_length=200, blank=True)

    # seperate each terms' model as ManyToManyField to collect user data in each term
    term1 = models.ManyToManyField('Term1')
    term2 = models.ManyToManyField('Term2')
    term3 = models.ManyToManyField('Term3')
    term4 = models.ManyToManyField('Term4')
    term5 = models.ManyToManyField('Term5')
    term6 = models.ManyToManyField('Term6')
    term7 = models.ManyToManyField('Term7')
    term8 = models.ManyToManyField('Term8')

    # create GPA model as ManyToManyField to collect user GPA
    gpa = models.ManyToManyField('GPA')

    # password = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.name


'''Now in each term (from 1 to 8) we will collect as CharField with max_length=255
1. subject name
2. unit 
3. grade (F-A)
4. GPA
'''


class Term1(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term2(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term3(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term4(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term5(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term6(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term7(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term8(models.Model):
    # collect term data by collecting (subject name, unit, grade and GPA)
    # เมื่อ user กรอกข้อมูล ใน term กรอก วิชา
    # subject, unit=3, grade=A เราจะมี model สำหรับเก็บข้อมูลดังกล่าวโดยสร้างไว้เป็น CharField มาก่อน
    # ที่ความยาวสูงสุดคือ 255 ตัวอักษร และจะทำการบันทึกเก็บเข้าไปในตัว model
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
