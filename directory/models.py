from django.db import models
from django.utils import timesince

# Create your models here.

class LongtermStatus(models.Model):
    LONGTERM_STATUS_CHOICES = (('O','Open'),
                              ('C','Closed'))
    LONGTERM_STATUS_DICT = { 'O' : 'Open',
                            'C' : 'Closed' }
    status = models.CharField(max_length=1, choices=LONGTERM_STATUS_CHOICES)
    permanent = models.NullBooleanField(default=True)

    def __unicode__(self):
        if self.permanent:
            return self.LONGTERM_STATUS_DICT[self.status]+' (permanent)'
        else:
            return self.LONGTERM_STATUS_DICT[self.status]+' (temprorary)'

class CurrentStatus(models.Model):
    # this COULD be a boolean now, but leaving open the possibility of having
    # more than two states.
    CURRENT_STATUS_CHOICES = (('A','Resources Available'),
                              ('U','No Resources Available'))
    CURRENT_STATUS_DICT = { 'A' : 'Resources Available',
                            'U' : 'No Resources Available' }
    status = models.CharField(max_length=1, choices=CURRENT_STATUS_CHOICES)

    def __unicode__(self):
        return self.CURRENT_STATUS_DICT[self.status]

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=True,
            blank=True, null=True)

    def __unicode__(self):
        return self.last_name+', '+self.first_name+' ('+self.email+')'

class Location(models.Model):
    street_one = models.CharField(max_length=50,null=True,blank=True)
    street_two = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=2,null=True,blank=True)
    zip_code = models.IntegerField(max_length=5,null=True,blank=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=True,
            blank=True, null=True)

class Resource(models.Model):
    name = models.CharField(max_length=255)
    homepage = models.URLField(null=True, blank=True)
    longterm_status = models.ForeignKey(LongtermStatus,
            on_delete=models.PROTECT, null=True, blank= True)
    current_status = models.ManyToManyField(CurrentStatus,
            through='StatusUpdate', null=True, blank=True)
    tags = models.ManyToManyField(Tag,null=True,blank=True)
    locations = models.ForeignKey(Location,null=True,blank=True)
    contacts = models.ForeignKey(Contact,null=True,blank=True)

    #attributes
    transitional_housing = models.BooleanField(default=False)
    affordable_housing = models.BooleanField(default=False)
    drop_in = models.BooleanField(default=False)
    men = models.BooleanField(default=False)
    women = models.BooleanField(default=False)
    mother_and_child = models.BooleanField(default=False)
    father_and_child = models.BooleanField(default=False)
    under_18 = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    showers = models.BooleanField(default=False)
    clothing = models.BooleanField(default=False)
    transportation = models.BooleanField(default=False)
    telephones = models.BooleanField(default=False)
    education_training = models.BooleanField(default=False)
    drug_rehab = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    case_management = models.BooleanField(default=False)
    health_center = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    mental_health = models.BooleanField(default=False)
    dental = models.BooleanField(default=False)
    job_attire = models.BooleanField(default=False)
    job_training = models.BooleanField(default=False)
    career_center = models.BooleanField(default=False)
    bike_repair = models.BooleanField(default=False)
    social_services = models.BooleanField(default=False)
    wheelchair_repair = models.BooleanField(default=False)
    mail_pickup = models.BooleanField(default=False)
    computer_center = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class StatusUpdate(models.Model):
    current_status = models.ForeignKey(CurrentStatus)
    resource = models.ForeignKey(Resource)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    # could also include the person/phone who reported the status?

    def __unicode__(self):
        return ' '.join([self.current_status,'('+timesince(self.timestamp)+' ago)'])

