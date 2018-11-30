from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    Category = models.CharField(max_length=300)
    Title = models.CharField(max_length=250)
    Date = models.CharField(max_length=500)
    Times = models.CharField(max_length=100)
    PictureLink = models.CharField(max_length=3000)
    AdmissionFee = models.IntegerField()
    Description = models.CharField(max_length=40000)
    Location = models.CharField(max_length=3000)
    Phone = models.CharField(max_length=20)
    AgeRestriction = models.IntegerField()
    WebsiteLink = models.CharField(max_length=3000)

    def __str__(self):
        return self.Title + " - " + self.Date

    def toJSON(self):
        dictOfAttributes = {
            "Category": self.Category,
            "Title": self.Title,
            "Date": self.Date,
            "Times": self.Times,
            "PictureLink": self.PictureLink,
            "AdmissionFee": self.AdmissionFee,
            "Description": self.Description,
            "Location": self.Location,
            "Phone": self.Phone,
            "AgeRestriction": self.AgeRestriction,
            "WebsiteLink": self.WebsiteLink
        }
        return dictOfAttributes
