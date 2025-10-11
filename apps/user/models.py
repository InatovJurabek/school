from django.db import models

class Region(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title_uz
    


class District(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_uz


class School(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_uz



class Subject(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title_uz
    
    
    
    
class Specialization(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)


    def __str__(self):
        return self.title_uz


