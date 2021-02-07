from django.db import models


class Method(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=50, blank=True)
    path = models.TextField(blank=True)
    airtable_id = models.CharField(max_length=50, default='none', blank=True)

    def __str__(self):
        return self.name


class Psychotherapist(models.Model):
    airtable_id = models.CharField(max_length=50, unique=True, default='none')
    name = models.CharField(max_length=100, blank=True)
    methods = models.ManyToManyField(Method, blank=True)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )

    def __str__(self):
        return self.name


class RawData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    def __str__(self):
        return str(self.date)
