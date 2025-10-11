from django.db import models



class Grade(models.Model):
    grade_level = models.IntegerField()
    description_uz = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.grade_level)


class Subject(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return self.title_uz
    

class GradeSubject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lesson_count = models.IntegerField()
    
    
    
class Topic(models.Model):
    grade_subject_id = models.ForeignKey(GradeSubject, on_delete=models.CASCADE)
    description_uz = models.TextField(blank = True , null = True)
    description_ru = models.TextField(blank = True , null = True)
    description_en = models.TextField(blank = True , null = True)
    title_uz = models.CharField(max_length=300)
    title_ru = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    order = models.IntegerField()
    
    
    def __str__(self):
        return self.title_uz


class Lesson(models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=300)
    title_ru = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    order = models.IntegerField()
    
    
    def __str__(self):
        return self.title