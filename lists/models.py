from django.db import models

class Userinfo(models.Model):
    #objects = None
    objects = None
    name = models.TextField(max_length=200, blank=True)
    #password = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.name
    #term1
    term1_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term1_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term1_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term1_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term1_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term1_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term1_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term1_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term1_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term1_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)



'''class Item(models.Model):
    text = models.TextField(default='')'''