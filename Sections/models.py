from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    title = models.CharField(max_length=100)
    score = models.IntegerField()

class Languages(models.Model):
    title = models.CharField(max_length=100)
    score = models.IntegerField()

class Education(models.Model):
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

class Contact(models.Model):
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField()