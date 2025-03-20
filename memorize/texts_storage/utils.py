from django.conf import settings
from fnmatch import fnmatch
import os
from bs4 import BeautifulSoup



# Функция для оборачивания слов в тег

def wrap_words_in_tag(element, tag_name):

    for text_node in element.find_all(string=True):# Находим все текстовые узлы
        if text_node.strip():  # Игнорируем пустые текстовые узлы
                
                words = text_node.split()  # Разделяем текст на слова
                wrapped_words = [f"<{tag_name}>{word}</{tag_name}>" for word in words]  # Обёртываем каждое слово
                new_text = " ".join(wrapped_words)  # Соединяем слова обратно
                text_node.replace_with(BeautifulSoup(new_text, 'html.parser'))  # Заменяем исходный текст

def savy_html(uploaded_file):
    with open(os.path.join(settings.MEDIA_ROOT, uploaded_file),'r', encoding='utf-8') as file:
        data = file.read()

    soup = BeautifulSoup(data, 'html.parser')
    
        
    # Применяем функцию ко всем элементам body
    chunk = len(soup.body.find_all())//100
    print(len(soup.body.find_all()))
    i = 0
    for element in soup.body.find_all():
        i+=1
        print(i)
        for c, ch in enumerate(element.contents):
            st = element.contents[c].string
            if ch == st and ch != ' ':
                wrap_words_in_tag(element, 'w  class= "hover-text-warning"')

    for a_tag in soup.find_all('a'):
        if a_tag.get('target') == '_self': continue
        if a_tag.get('href'):
            if a_tag.get('href')[0] == '#': continue
        a_tag['target'] = '_blank'

    
    data = str(soup)
    if not fnmatch(data, '{% verbatim %}*{% endverbatim %}'):
        data = '{% verbatim %}' + data + '{% endverbatim %}'
    with open(os.path.join(settings.MEDIA_ROOT, uploaded_file),'w', encoding='utf-8') as file:
        file.write(data)
    
        