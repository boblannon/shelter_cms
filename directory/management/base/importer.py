import csv
import re, os
import json

from dateutil.parser import parse

from django.conf import settings

import gdata.docs
import gdata.docs.service
import gdata.spreadsheet.service

from directory.models import Contact, Location, Resource, LongtermStatus, Tag

DATA_DIR = os.path.join(settings.PROJECT_ROOT, 'data')
JSON_DIR = os.path.join(DATA_DIR,'json')
IN = os.path.join(DATA_DIR,'IN')
FAILED = os.path.join(DATA_DIR,'FAILED')
OUT = os.path.join(DATA_DIR,'OUT')

csv_fields = [                               
 'Mother&Children',
 'CaseManagement',
 'Wheelchair Repair',
 'Organization',
 'EligibleClients',
 'Affordable Housing',
 'Status',
 'Health Center',
 'Father&Children',
 'Families',
 'Food',
 'Under 18',
 'Dental',
 'Men',
 'Email',
 'Hours',
 'Phone',
 'Job Attire',
 'Social Services',
 'Women',
 'URL',
 'DrugRehab',
 'Computer Center',
 'Emergency Shelter',
 'Telephones',
 'Transportation',
 'Laundry',
 'Mental Health',
 'EducationTraining',
 'Mail pick up',
 'Career Center',
 'Tag',
 'Job Training',
 'Showers',
 'Bike Repair',
 'Drop-in Center',
 'Transitional Housing',
 'Clothing']

# class CSVImporter():
# 
#     def __init__(self):
#         self.infile = os.path.join(IN,'master_resource_list.csv')
# 
#     def upload(self):
#         try:
#             dr = csv.DictReader(self.infile)
#             for e in dr:
#                 location = Location(street_one=e['Address'],
#                                         city=e['City'],
#                                         state=e['State'],
#                                         zip_code=int(e['Zipcode']),
#                                         lat=float(e['Lat']),
#                                         lon=float(e['Long']))

def get_truthy(value):
    if value:
        try:
            return bool(int(value))
        except ValueError:
            if len(value) and value.strip().lower()[0] == 't':
                return True
            else:
                return False
    else:
        return False

class GDATAError(Exception):

    def __init__(self,query):
        self.query = query
    def __str__(self):
        return 

class GDATAImporter():
    
    def __init__(self):
        self.username = settings.GDATA_USERNAME
        self.password = settings.GDATA_PASSWORD
        self.app_name = settings.GDATA_APPNAME
        self.login_to_gdata()

    def login_to_gdata(self):
        self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
        self.gd_client.email = self.username
        self.gd_client.password = self.password
        self.gd_client.source = 'sheltr_cms'
        self.gd_client.ProgrammaticLogin()

    def read_feed_for_unique_result(self,feed,query=None):
        num_results = int(feed.total_results.text)
        if num_results == 1:
            return feed.entry[0]
        if num_results > 1:
            if query:
                print 'found more than one result for "{0}"'.format(str(query))
            else:
                print 'found more than one result!'
            raise Exception
        elif num_results == 0:
            if query:
                print 'found no results for "{0}"'.format(str(query))
            else:
                print 'found no results!'
            raise Exception
        else:
            if query:
                print 'something went wrong at "{0}"'.format(str(query))
            else:
                print 'something went wrong'
            raise Exception

    def read_feed_for_at_least_one_result(self,feed,query=None):
        num_results = int(feed.total_results.text)
        if num_results >= 1:
            return feed
        elif num_results == 0:
            if query:
                print 'found no results for "{0}"'.format(str(query))
            else:
                print 'found no results!'
            raise Exception
        else:
            if query:
                print 'something went wrong at "{0}"'.format(str(query))
            else:
                print 'something went wrong'
            raise Exception

    def find_spreadsheet(self,doc_name):
        q = gdata.spreadsheet.service.DocumentQuery()
        q['title'] = doc_name
        q['title-exact'] = 'true'
        feed = self.gd_client.GetSpreadsheetsFeed(query=q)
        self.spreadsheet = self.read_feed_for_unique_result(feed,query=q)
        self.spreadsheet_id = self.spreadsheet.id.text.rsplit('/',1)[1]

    def last_updated(self):
        dt = parse(self.spreadsheet.updated.text)
        return dt

    def select_worksheet(self):
        feed = self.gd_client.GetWorksheetsFeed(self.spreadsheet_id)
        # always take the first sheet
        self.worksheet = self.read_feed_for_at_least_one_result(feed).entry[0]
        self.worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

    def get_data(self):
        rows = self.gd_client.GetListFeed(self.spreadsheet_id,
                                          self.worksheet_id).entry
        self.data = []
        for row in rows:
            self.data.append({k:v.text for k,v in row.custom.iteritems()})

    def save_json_data(self):
        fout = open(os.path.join(JSON_DIR,self.spreadsheet_id),'w')
        json.dump(self.data,fout)

    def upload(self):
        for d in self.data:
            # Parse Location fields
            location, created = Location.objects.get_or_create( 
                                street_one      = d['address'],
                                city            = d['city'],
                                state           = d['state'],
                                zip_code        = d['zipcode'],
                                lat             = d['lat'],
                                lon             = d['long'],
                                last_updated    = self.last_updated())
            if created:
                location.save()
            # Parse contact fields
            contact, created = Contact.objects.get_or_create(  
                                first_name      = d['contactfirstname'],
                                last_name       = d['contactlastname'],
                                phone           = d['phone'],
                                email           = d['email'],
                                last_updated    = self.last_updated())
            if created:
                contact.save()
            # Create resource
            resource = Resource(    
                    name                    =   d['organization']                      ,
                    homepage                =   d['url']                               ,
                    transitional_housing    =   get_truthy(d['transitionalhousing']   ),
                    affordable_housing      =   get_truthy(d['affordablehousing']     ),
                    drop_in                 =   get_truthy(d['drop-incenter']         ),
                    men                     =   get_truthy(d['men']                   ),
                    women                   =   get_truthy(d['women']                 ),
                    mother_and_child        =   get_truthy(d['motherchildren']        ),
                    father_and_child        =   get_truthy(d['fatherchildren']        ),
                    under_18                =   get_truthy(d['under18']               ),
                    family                  =   get_truthy(d['families']              ),
                    showers                 =   get_truthy(d['showers']               ),
                    clothing                =   get_truthy(d['clothing']              ),
                    transportation          =   get_truthy(d['transportation']        ),
                    telephones              =   get_truthy(d['telephones']            ),
                    education_training      =   get_truthy(d['educationtraining']     ),
                    drug_rehab              =   get_truthy(d['drugrehab']             ),
                    food                    =   get_truthy(d['food']                  ),
                    case_management         =   get_truthy(d['casemanagement']        ),
                    health_center           =   get_truthy(d['healthcenter']          ),
                    laundry                 =   get_truthy(d['laundry']               ),
                    mental_health           =   get_truthy(d['mentalhealth']          ),
                    dental                  =   get_truthy(d['dental']                ),
                    job_attire              =   get_truthy(d['jobattire']             ),
                    job_training            =   get_truthy(d['jobtraining']           ),
                    career_center           =   get_truthy(d['careercenter']          ),
                    bike_repair             =   get_truthy(d['bikerepair']            ),
                    social_services         =   get_truthy(d['socialservices']        ),
                    wheelchair_repair       =   get_truthy(d['wheelchairrepair']      ),
                    mail_pickup             =   get_truthy(d['mailpickup']            ),
                    computer_center         =   get_truthy(d['computercenter']        )    )
            resource.save()
            # add tags, comma-delimited
            if d['tag']:
                tagset = [t.strip() for t in d['tag'].split(',')]
                for t in tagset:
                    tag,created = Tag.objects.get_or_create(name=t)
                    if created:
                        tag.save()
                    resource.tags.add(tag)
            # add location and contact
            resource.locations = location
            resource.contacts = contact
            # save
            resource.save()        
