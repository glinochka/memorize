from django.conf import settings
from fnmatch import fnmatch
import os
from bs4 import BeautifulSoup
from bs4.element import NavigableString

def wrap_words_in_tag(text_node, tag_name, is_a, count):
    words = text_node.split()
    wrapped_words = []

    for word in words:
        count+=1
        wrapped_words += [f"<{tag_name} id = '{count}'>{word}</{tag_name}>"]

    if is_a:
        new_text = '&nbsp;' + " ".join(wrapped_words) + '&nbsp;'
    else:
        new_text = " ".join(wrapped_words) 

    text_node.replace_with(BeautifulSoup(new_text, 'html.parser'))

    return count



def wrap_w(soup):
    count = 0
    for i in soup.body.descendants:
        if type(i) == NavigableString and not i.isspace():
            count = wrap_words_in_tag(i, 'w',  any('a' == p.name for p in i.parents), count)

    return str(soup)

def addtempls(html, style, button, script):
    html = html.replace('</head>', style+'</head>').replace('</body>', script+'</body>').replace('</body>', button+'</body>')
    return html



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
    data = '{%load static%}' + data.replace('{{','{_{').replace('}}','}_}')

    data = addtempls(data, '{% include "style.html" %}', '{% include "button.html" %}', '{% include "script.html" %}')
    
    with open(os.path.join(settings.MEDIA_ROOT, uploaded_file),'w', encoding='utf-8') as file:
        file.write(data)
    
        