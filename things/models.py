from django.db import models

# Create your models here.

class Site(models.Model):
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    intro = models.TextField(max_length=1000)
    def __unicode__(self):
        return unicode(self.start_date)

class Thing(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    complete = models.BooleanField()
    complete_date = models.DateTimeField('completion date', blank=True, null=True)
    private = models.BooleanField()
    subthing = models.ForeignKey('self', blank=True, null=True)
    site = models.ForeignKey(Site)
    def __unicode__(self):
        return unicode(self.name)

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    things = models.ManyToManyField(Thing)
    def __unicode__(self):
        return unicode(self.title)

