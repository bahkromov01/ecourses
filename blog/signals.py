import json

from django.db.models.signals import post_save
from django.dispatch import receiver
import os

from blog.models import Blog_list
from confic.settings import BASE_DIR


@receiver(post_save, sender=Blog_list)
def blog_save(sender, instance, created,  **kwargs):
    if created:
        print(f'{instance.title} is created! ')
        print(kwargs)
    else:
        print('Course updated')


def blog_delete(sender, instance, **kwargs):
    file = os.path.join(BASE_DIR, 'blog/delete', f'blog_{instance.id}.json')

    blog_data = {
        'id': instance.id,
        'title': instance.title,
        'author': instance.author,
        'post_date': instance.post_date,
    }
    with open(file, mode='w') as file_json:
        json.dump(blog_data, file_json, indent=4)
        print(f'{instance.title} was deleted ! ')