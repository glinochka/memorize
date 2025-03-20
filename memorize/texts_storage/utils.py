from django.conf import settings
from fnmatch import fnmatch
import os

def savy_html(uploaded_file):
    with open(os.path.join(settings.MEDIA_ROOT, uploaded_file),'r', encoding='utf-8') as file:
        data = file.read()
    if not fnmatch(data, '{% verbatim %}*{% endverbatim %}'):
        data = '{% verbatim %}' + data + '{% endverbatim %}'
    with open(os.path.join(settings.MEDIA_ROOT, uploaded_file),'w', encoding='utf-8') as file:
        file.write(data)
    
        