#!usr/bin/env python3
from airtable import Airtable
from profiles.models import Psychotherapist, Photo, Method, RawData
import os

from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')
AIRTABLE_DB_ID = os.getenv('AIRTABLE_DB_ID')
TABLE_NAME = os.getenv('TABLE_NAME')
VIEW = 'Grid view'


airtable = Airtable(AIRTABLE_DB_ID, TABLE_NAME, api_key=API_KEY)

table_data = airtable.get_all(view=VIEW)
print(table_data[3])

raw_data = RawData()
raw_data.data = table_data
raw_data.save()

therapists_in_airtable = set()
therapists_in_local_db = set()

for person in table_data:
    therapists_in_airtable.add(person['id'])
    updated_values = {}
    if 'Имя' in person['fields'].keys():
        updated_values.update({'name': person['fields']['Имя']})
    if 'Фотография' in person['fields'].keys():
        photo, created = Photo.objects.get_or_create(
            airtable_id=person['fields']['Фотография'][0]['id'],
            name=person['fields']['Фотография'][0]['filename'],
            path=person['fields']['Фотография'][0]['url'],
        )

                    # therapist = Psychotherapist()
                    # therapist.airtable_id = person['id']
                    # therapist.name = person['fields']['Имя']
                    # therapist.photo = Photo.objects.get(pk=photo.pk)
                    # therapist.save()
        updated_values.update({'photo': Photo.objects.get(pk=photo.pk)})

    therapist, created = Psychotherapist.objects.update_or_create(
        airtable_id=person['id'], defaults=updated_values
    )
                    # therapist.name = person['fields']['Имя']
                    # therapist.photo = Photo.objects.get(pk=photo.pk)
    if 'Методы' in person['fields'].keys():
        updated_methods = []
        for method_name in person['fields']['Методы']:
            method, created = Method.objects.get_or_create(name=method_name)
            updated_methods.append(method.pk)
        therapist.methods.clear()
        therapist.methods.set(updated_methods)
        therapist.save()
    else:
        therapist.methods.clear()

    therapists = Psychotherapist.objects.all()
    for elem in therapists:
        therapists_in_local_db.add(elem.airtable_id)
    removed_therapists = therapists_in_local_db - therapists_in_airtable


for therapist_id in removed_therapists:
    Psychotherapist.objects.get(airtable_id=therapist_id).delete()




