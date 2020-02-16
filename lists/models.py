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

    # term2
    term2_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term2_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term2_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term2_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term2_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term2_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term2_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term2_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term2_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term2_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)

    # term3
    term3_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term3_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term3_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term3_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term3_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term3_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term3_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term3_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term3_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term3_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)

    # term4
    term4_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term4_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term4_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term4_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term4_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term4_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term4_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term4_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term4_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term4_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)

    # term5
    term5_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term5_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term5_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term5_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term5_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term5_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term5_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term5_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term5_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term5_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)

    # term6
    term6_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term6_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term6_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term6_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term6_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term6_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term6_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term6_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term6_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term6_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)

    # term7
    term7_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term7_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term7_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term7_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term7_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term7_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term7_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term7_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term7_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term7_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)

    # term8
    term8_subject_1 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_1_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_1_grade = models.TextField(max_length=200, blank=True, null=True)

    term8_subject_2 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_2_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_2_grade = models.TextField(max_length=200, blank=True, null=True)

    term8_subject_3 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_3_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_3_grade = models.TextField(max_length=200, blank=True, null=True)

    term8_subject_4 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_4_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_4_grade = models.TextField(max_length=200, blank=True, null=True)

    term8_subject_5 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_5_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_5_grade = models.TextField(max_length=200, blank=True, null=True)

    term8_subject_6 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_6_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_6_grade = models.TextField(max_length=200, blank=True, null=True)

    term8_subject_7 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_7_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_7_grade = models.TextField(max_length=200, blank=True, null=True)

    term8_subject_8 = models.TextField(max_length=200, blank=True, null=True)
    term8_subject_8_unit = models.TextField(max_length=10, blank=True, null=True)
    term8_subject_8_grade = models.TextField(max_length=200, blank=True, null=True)



'''class Item(models.Model):
    text = models.TextField(default='')'''