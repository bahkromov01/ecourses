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
        subject = f'HI{instance.name}'
        message = 'Your teachers has been created. Thank you!'
        from_email = (settings.EMAIL_HOST_USER)
        to_email =[instance.email]
        try:
            send_mail(subject, message, from_email, to_email)
            print(f'Mail sent to {instance.email}')
        except Exception as e:
            raise f'Error sending email: {e}'


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

