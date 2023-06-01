from django.db import models
import datetime

# Create your models here.


class FAQ(models.Model):
    """The FAQ models is responsible for storing data
    about questions and their answers. Also, it has is_on_homepage variable,
    which will answer should we show in homepage yes or no"""
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=1000)
    is_on_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class Visitors(models.Model):
    """The visitors models are responsible for storing data about
     visitor's ip and how many times they visited"""
    ip_address = models.CharField(max_length=255)
    visited_times = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'

    def __str__(self):
        return f'Visitor: {self.ip_address}'


class VisitorsTime(models.Model):
    """The visitors time is model for storing visitor time, since one
    visitor could have numerous time of visiting"""
    Visitors = models.ForeignKey(Visitors, on_delete=models.CASCADE, related_name='visitor_times')
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.Visitors.ip_address

    class Meta:
        verbose_name = 'Visited time'
        verbose_name_plural = 'Visited times'


class ContactQuestions(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=510, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    is_answered = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Contact question'
        verbose_name_plural = 'Contact questions'
