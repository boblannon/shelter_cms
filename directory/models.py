from django.db import models
from django.utils import timesince

# Create your models here.

class LongtermStatus(models.Model):
    LONGTERM_STATUS_CHOICES = (('O','Open'),
                              ('C','Closed'))
    LONGTERM_STATUS_DICT = { 'O' : 'Open',
                            'C' : 'Closed' }
    status = models.CharField(max_length=1, choices=CURRENT_STATUS_CHOICES)
    permanent = models.NullBooleanField(default=True)

class CurrentStatus(models.Model):
    # this COULD be a boolean now, but leaving open the possibility of having
    # more than two states.
    CURRENT_STATUS_CHOICES = (('A','Resources Available'),
                              ('U','No Resources Available'))
    CURRENT_STATUS_DICT = { 'A' : 'Resources Available',
                            'U' : 'No Resources Available' }
    status = models.CharField(max_length=1, choices=CURRENT_STATUS_CHOICES)

class StatusUpdate(models.Model):
    current_status = models.ForeignKey(CurrentStatus)
    resource = models.ForeignKey(Resource)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    # could also include the person/phone who reported the status?

    def __unicode__(self):
        return ' '.join([self.current_status,'('+timesince(self.timestamp)+' ago)'])

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=True,
            blank=True, null=True)

    def __unicode__(self):
        return self.last_name+', '+self.first_name+' ('+self.email+')'

class Location(models.Model):
    street_one = models.CharField(max_length=50,null=True,blank=True)
    street_two = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharFied(max_length=2,null=True,blank=True)
    zip_code = models.IntegerField(max_length=5,null=True,blank=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=True,
            blank=True, null=True)

class Resource(models.Model):
    name = models.CharField(max_length=255)
    homepage = models.URLField()
    longterm_status = models.ForeignKey(LongtermStatus,
            on_delete=models.PROTECT, null=True, blank= True)
    current_status = models.ForeignKey(CurrentStatus, through='StatusUpdate')
    tags = models.ManyToManyField(Tag,null=True,blank=True)
    locations = models.ManyToManyField(Location,null=True,blank=True)
    contacts = models.ManyToManyField(Contact,null=True,blank=True)

    #attributes
    transitional_housing = models.BooleanField()
    affordable_housing = models.BooleanField()
    drop_in = models.BooleanField()
    men = models.BooleanField()
    women = models.BooleanField()
    mother_and_child = models.BooleanField()
    father_and_child = models.BooleanField()
    under_18 = models.BooleanField()
    family = models.BooleanField()
    showers = models.BooleanField()
    clothing = models.BooleanField()
    transportation = models.BooleanField()
    telephones = models.BooleanField()
    education_training = models.BooleanField()
    drug_rehab = models.BooleanField()
    food = models.BooleanField()
    case_management = models.BooleanField()
    health_center = models.BooleanField()
    laundry = models.BooleanField()
    mental_health = models.BooleanField()
    dental = models.BooleanField()
    transitional_housing = models.BooleanField()
    job_attire = models.BooleanField()
    job_training = models.BooleanField()
    career_center = models.BooleanField()
    bike_repair = models.BooleanField()
    social_services = models.BooleanField()
    wheelchair_repair = models.BooleanField()
    mail_pickup = models.BooleanField()
    computer_center = models.BooleanField()
