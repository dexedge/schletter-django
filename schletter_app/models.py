from django.db import models
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    """Schletter About page"""
    content = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'About'

class Date(models.Model):
    date = models.DateField(primary_key=True)

    def __str__(self):
        date = self.date.strftime('%a, %-d %b %Y')
        return date

class Event(models.Model):
    """Schletter Event model"""
    date  = models.ForeignKey(Date, on_delete=models.CASCADE)
    event_order = models.PositiveSmallIntegerField(
        default = 0, blank = False, null = False, db_index = True,
    )
    title = models.CharField(max_length=100)
    theater = models.CharField(max_length=3)
    company = models.CharField(max_length=10)
    event_type = models.CharField(max_length=50)
    hadamowsky = models.CharField(max_length=5)
    morrow = models.CharField(max_length=5)
    notes = RichTextField(null=True, blank=True)
    
    def __str__(self):
        event = str(self.date) + ", " + self.title
        return event

    def get_absolute_url(self):
        return reverse('schletter_app:event', kwargs={'pk': self.pk})
        
    class Meta:
        ordering = ['event_order']
    
class Work(models.Model):
    events = models.ManyToManyField(Event, through="WorkEvent")
    title = models.CharField(max_length=100)
    source_title = models.CharField(max_length=100, null=True, blank=True)
    sort_title = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=75)
    source_genre = models.CharField(max_length=75, null=True, blank=True)
    notes = RichTextField(null=True, blank=True)
    title_page = models.ImageField(null=True, blank=True, upload_to="images/")
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('schletter_app:work', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['sort_title']

class WorkEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event.date) + ", " + self.event.title 
    
    class Meta:
        ordering = ['event__event_order',]

class Author(models.Model):
    works = models.ManyToManyField(Work, through="AuthorWork", related_name="authorworks")
    last_name = models.CharField(max_length=100)
    first_names = models.CharField(max_length=200)
    birth = models.IntegerField()
    death = models.IntegerField()
    notes = RichTextField(null=True, blank=True)

    def __str__(self):
        if self.first_names == "NA":
            return self.last_name
        else:
            return self.last_name + ", " + self.first_names

    def get_absolute_url(self):
        return reverse('schletter_app:author', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['last_name', 'first_names']

class AuthorWork(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.author.last_name + ", " + self.work.title
    
    class Meta:
        ordering = ['author__last_name',]
    

class Composer(models.Model):
    works = models.ManyToManyField(Work, through="ComposerWork",related_name="composerworks")
    last_name = models.CharField(max_length=100)
    first_names = models.CharField(max_length=200)
    birth = models.IntegerField()
    death = models.IntegerField()
    notes = RichTextField(null=True, blank=True)

    def __str__(self):
        if self.first_names == "NA":
            return self.last_name
        else:
            return self.last_name + ", " + self.first_names

    def get_absolute_url(self):
        return reverse('schletter_app:composer', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['last_name', 'first_names']

class ComposerWork(models.Model):
    id = models.IntegerField(primary_key=True)
    composer = models.ForeignKey(Composer, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.composer.last_name + ", " + self.work.title
    
    class Meta:
        ordering = ['composer__last_name',]
