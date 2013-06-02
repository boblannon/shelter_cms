from django.contrib import admin
from django.db import models

from directory.models import * #sorry, need to save time

class LocationInline(admin.StackedInline):
    model = Location
    extra = 1

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1

class ContactAdmin(admin.ModelAdmin):
    model = Contact

class LocationAdmin(admin.ModelAdmin):
    model = Location

class ResourceAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields': (('name', 'homepage', 'longterm_status', 
                    'current_status'))
                }),
            ('Attributes', {
                'fields': (('transitional_housing',
                    'affordable_housing',
                    'drop_in',
                    'men',
                    'women',
                    'mother_and_child',
                    'father_and_child',
                    'under_18',
                    'family',
                    'showers',
                    'clothing',
                    'transportation',
                    'telephones',
                    'education_training',
                    'drug_rehab',
                    'food',
                    'case_management',
                    'health_center',
                    'laundry',
                    'mental_health',
                    'dental',
                    'transitional_housing',
                    'job_attire',
                    'job_training',
                    'career_center',
                    'bike_repair',
                    'social_services',
                    'wheelchair_repair',
                    'mail_pickup',
                    'computer_center'))
                })
    
    inlines = [
            ContactInline,
            LocationInline,
            ]
    list_display = ('__unicode__',
        'homepage',
        'longterm_status',
        'current_status',
        'tags',
        'locations',
        'contacts',
        'transitional_housing',
        'affordable_housing',
        'drop_in',
        'men',
        'women',
        'mother_and_child',
        'father_and_child',
        'under_18',
        'family',
        'showers',
        'clothing',
        'transportation',
        'telephones',
        'education_training',
        'drug_rehab',
        'food',
        'case_management',
        'health_center',
        'laundry',
        'mental_health',
        'dental',
        'transitional_housing',
        'job_attire',
        'job_training',
        'career_center',
        'bike_repair',
        'social_services',
        'wheelchair_repair',
        'mail_pickup',
        'computer_center') 
    list_editable = ('__unicode__',
        'homepage',
        'longterm_status',
        'current_status',
        'tags',
        'locations',
        'contacts',
        'transitional_housing',
        'affordable_housing',
        'drop_in',
        'men',
        'women',
        'mother_and_child',
        'father_and_child',
        'under_18',
        'family',
        'showers',
        'clothing',
        'transportation',
        'telephones',
        'education_training',
        'drug_rehab',
        'food',
        'case_management',
        'health_center',
        'laundry',
        'mental_health',
        'dental',
        'transitional_housing',
        'job_attire',
        'job_training',
        'career_center',
        'bike_repair',
        'social_services',
        'wheelchair_repair',
        'mail_pickup',
        'computer_center')
    list_per_page = 100
    list_filter = ('longterm_status','current_status','tags')
    search_fields = ['name','homepage']

admin.site.register(Resource,ResourceAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Tag)
admin.site.register(CurrentStatus)
admin.site.register(LongtermStatus)
