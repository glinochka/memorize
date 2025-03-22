from django.conf import settings
from fnmatch import fnmatch
import os
from bs4 import BeautifulSoup
from bs4.element import NavigableString

def wrap_words_in_tag(text_node, tag_name, is_a):
    words = text_node.split()  
    wrapped_words = [f"<{tag_name}>{word}</{tag_name}>" for word in words] 

    if is_a:
        new_text = '&nbsp;' + " ".join(wrapped_words) + '&nbsp;'
    else:
        new_text = " ".join(wrapped_words) 

    text_node.replace_with(BeautifulSoup(new_text, 'html.parser'))



def wrap_w(soup):
    for i in soup.body.descendants:
        if type(i) == NavigableString and not i.isspace():
            wrap_words_in_tag(i, 'w',  any('a' == p.name for p in i.parents))

    return str(soup)




def savy_html(uploaded_file):
    with open(os.path.join(settings.MEDIA_ROOT, uploaded_file),'r', encoding='utf-8') as file:
        data = file.read()

    soup = BeautifulSoup(data, 'html.parser')
    
    for a_tag in soup.find_all('a'):
        if a_tag.get('target') == '_self': continue
        if a_tag.get('href'):
            if a_tag.get('href')[0] == '#': continue
        a_tag['target'] = '_blank'

    data = wrap_w(soup)

    if not fnmatch(data, '{% verbatim %}*{% endverbatim %}'):
        data = '{% verbatim %}' + data + '{% endverbatim %}'

    with open(os.path.join(settings.MEDIA_ROOT, uploaded_file),'w', encoding='utf-8') as file:
        file.write(data)
    
        