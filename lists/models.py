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

class Term1(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph

    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term2(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term3(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term4(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term5(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term6(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term7(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)


class Term8(models.Model):
    # example model จะถูกนำไปใช้งานใน views.py
    # อย่างใน function การคำนวณเกรด
    # 1 เราจะเช็คว่า objects ใน term นั้นต้อง ไม่เกิน 9 ตัว
    # 2 จากนั้นทำการเช็คว่า objects ใน term นั้นมีความยาวเท่ากับ 0 หรือไม่
    # 2.1 หากใช่ให้ทำการสร้าง objects ใน term 9 ตัวโดยแต่ละตัวจะ เก็บ (subject, unit, grade และ GPA)
    # 2.2 หากไม่ให้ทำการอัพเดท ข้อมูลที่มีอยู่ให้เป็นข้อมูลใหม่ที่ user กรอกเข้ามานั่นเอง

    # นำข้อมูลที่ User กรกอก ซึ่งคือ (subject, unit, grade)
    # และ GPA (ที่โปรแกรมคำนวณให้)
    # มาแสดงในหน้า Result ของแต่ละ term ที่ user เลือก
    # โดยแสดงเป็น (subject, unit, grade, GPA และที่เพิ่มเข้ามาคือการคำนวณ GPAX และนำมาแสดง)

    # หน้ากราฟเช่นกันจะนำ User (subject, unit, grade and GPA) มาแสดงกราฟในหน้า Graph
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
