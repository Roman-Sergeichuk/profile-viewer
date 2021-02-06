from airtable import Airtable
from profiles.models import Psychotherapist, Photo, Method

airtable = Airtable('appcOFIiDWJc5AGoC', 'Psychotherapists', api_key='keyIhgqVF6a6dNQGn')

table_data = airtable.get_all(view='Grid view')


for person in table_data:

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
    updated_values = {'photo': Photo.objects.get(pk=photo.pk), 'name': person['fields']['Имя']}
    therapist, created = Psychotherapist.objects.update_or_create(
        airtable_id=person['id'], defaults=updated_values
    )
    # therapist.name = person['fields']['Имя']
    # therapist.photo = Photo.objects.get(pk=photo.pk)

    for method_name in person['fields']['Методы']:
        method, created = Method.objects.get_or_create(name=method_name)
        therapist.methods.add(method.pk)




