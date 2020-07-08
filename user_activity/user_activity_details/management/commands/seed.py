import random
import string 
import datetime
from django.core.management.base import BaseCommand
from user_activity_details import models
from faker import Faker

time_zone_list = ['Asia/Kolkata','America/Eirunepe','America/Boa_Vista','Europe/Kirov']

class Generate(object):
    def __init__(self):
        self.faker = Faker()

    def name(self):
        return self.faker.name()

    def unique_id(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k = 11))
		

class Command(BaseCommand):
    help = 'Create dummy data in database.'

    def get_datetime(self):
        difference_date = random.randint(1,100)
        minutes = random.randint(1,60)
        start_date = datetime.datetime.now() + datetime.timedelta(days=-difference_date)
        end_date = start_date + datetime.timedelta(minutes=minutes)
        return start_date,end_date

    def get_user_id(self):
        filter_data = models.UserDetail.objects.filter().values('id')
        return random.choice(list(filter_data.values()))['id']

    def create_user_details(self):
        generate = Generate()       
        records = []
        for _ in range(100):
            kwargs = {
                'id': generate.unique_id(),
                'name': generate.name(),
                'time_zone': random.choice(time_zone_list)
            }
            record = models.UserDetail(**kwargs)
            records.append(record)
        models.UserDetail.objects.bulk_create(records)      

    def create_user_activity(self):        
        records = []
        for _ in range(100):
            start_datetime, end_datetime = self.get_datetime()
            kwargs = {
                'user_id': self.get_user_id(),
                'start_time': start_datetime,
                'end_time': end_datetime
            }
            record = models.UserActivity(**kwargs)
            records.append(record)
        models.UserActivity.objects.bulk_create(records)      


    def handle(self, *args, **options):        
        self.create_user_details()
        self.create_user_activity()
        self.stdout.write(self.style.SUCCESS('User Details are created'))

