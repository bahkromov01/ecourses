import json
import os

from cffi.backend_ctypes import unicode
from django.core.mail import send_mail
from django.db.models import ImageField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from confic import settings
from confic.settings import BASE_DIR
from courses.models import Course




@receiver(post_save, sender=Course)
def courses_save(sender, instance, created,  **kwargs):
    if created:
        print(f'{instance.title} is created! ')
        print(kwargs)
    else:
        print('Course updated')


@receiver(post_delete, sender=Course)
def courses_delete(sender, instance, **kwargs):
    file = os.path.join(BASE_DIR, 'courses/delete', f'courses_{instance.id}.json')

    courses_data = {

        'id': instance.id,
        'title': instance.title,
        'description': instance.description,
        'number_of_students': instance. number_of_students,
        'price': instance.price,
        'duration': instance.duration,
    }
    with open(file, mode='w+') as file_json:
        json.dump(courses_data, file_json, indent=4)
        print(f'{instance.title} was deleted ! ')
