from datetime import timedelta

from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    month_to_learn = models.IntegerField()

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def save(self, *args, **kwargs):
        if self.name.lower() == 'java script':
            self.name = 'Java Script'
        super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number and self.phone_number.startswith('0') and len(self.phone_number) == 10:
            self.phone_number = '+996' + self.phone_number[1:]
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=100, null=True)
    has_own_notebook = models.BooleanField(default=False)
    preferred_os = models.CharField(max_length=10)


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100, null=True)
    experience = models.DateField()


class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def get_end_date(self):
        duration = self.language.month_to_learn
        end_date = self.date_started + timedelta(days = 30 * duration)
        return end_date
