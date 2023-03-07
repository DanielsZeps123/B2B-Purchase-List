from django.db import models

class Section(models.Model):
    section = models.CharField(max_length=50, default=None)
    # link = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.section

class Filter(models.Model):
    filter = models.CharField(max_length=50, default=None)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.filter) + " --- " + str(self.section.section)

# Create your models here.
