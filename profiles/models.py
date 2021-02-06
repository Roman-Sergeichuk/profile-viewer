from django.db import models


class Method(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=50)
    path = models.TextField()
    airtable_id = models.CharField(max_length=50, default='none')

    def __str__(self):
        return self.name


class Psychotherapist(models.Model):
    airtable_id = models.CharField(max_length=50, unique=True, default='none')
    name = models.CharField(max_length=100)
    methods = models.ManyToManyField(Method)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name


# class RawData(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     data = models.TextField()

