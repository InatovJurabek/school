from django.db import models
from django.utils.translation import gettext_lazy as _

class Region(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.title_uz

class District(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    percentage = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')
    is_all_districts = models.BooleanField(default=False) 

    def __str__(self):
        return self.title_uz

class School(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    percentage = models.IntegerField()
    male_students = models.IntegerField()
    female_students = models.IntegerField()
    total_students = models.IntegerField()
    teachers_count = models.IntegerField() 
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='schools')

    def __str__(self):
        return self.title_uz