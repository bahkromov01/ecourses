import json
import os

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from confic import settings
from confic.settings import BASE_DIR
from teachers.models import Teachers


@receiver(post_save, sender=Teachers)
def teachers_save(sender, instance, created,  **kwargs):
    if created:
        print(f'{instance.full_name} is created! ')
        print(kwargs)
    else:
        print('Course updated')


def teachers_delete(sender, instance, **kwargs):
    file = os.path.join(BASE_DIR, 'teachers/delete', f'teachers_{instance.id}.json')
    teachers_data = {
        'id': instance.id,
        'full_name': instance.full_name,
        'courses': instance.courses,
        'image': instance.image,
        'specialty': instance.specialty,
        'category': instance.category,
        'level': instance.level,
    }
    with open(file, mode='w') as file_json:
        json.dump(teachers_data, file_json, indent=4)
        print(f'{instance.full_name} was deleted ! ')

