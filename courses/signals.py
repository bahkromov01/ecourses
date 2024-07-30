import json
import os

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from confic import settings
from confic.settings import BASE_DIR
from courses.models import Course




@receiver(post_save, sender=Course)
def courses_save(sender, instance, created,  **kwargs):
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


def courses_delete(sender, instance, **kwargs):
    file = os.path.join(BASE_DIR, 'courses/delete', f'courses_{instance.id}.json')

    courses_data = {

        'id': instance.id,
        'title': instance.title,
        'description': instance.description,
        'number_of_students': instance. number_of_students,
        'price': instance.price,
        'duration': instance.duration,
        'image': instance.image,
        'video': instance.vedio,
        'category': instance.category
    }
    with open(file, mode='w') as file_json:
        json.dump(courses_data, file_json, indent=4)
        print(f'{instance.full_name} was deleted ! ')
