from bs4 import BeautifulSoup

with open('Dockerfile_reference___Docker_Docs.html','r', encoding='utf-8') as f:
    html_content = f.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Функция для оборачивания слов в тег
def wrap_words_in_tag(element, tag_name):

    for text_node in element.find_all(string=True):# Находим все текстовые узлы
        if text_node.strip():  # Игнорируем пустые текстовые узлы
                
                words = text_node.split()  # Разделяем текст на слова
                wrapped_words = [f"<{tag_name}>{word}</{tag_name}>" for word in words]  # Обёртываем каждое слово
                new_text = " ".join(wrapped_words)  # Соединяем слова обратно
                text_node.replace_with(BeautifulSoup(new_text, 'html.parser'))  # Заменяем исходный текст
        
# Применяем функцию ко всем элементам body
for element in soup.body.find_all():
    for c, ch in enumerate(element.contents):
        
        st = element.contents[c].string
        if ch == st and ch != ' ':
            wrap_words_in_tag(element, 'w  class= "hover-text-warning"')

with open('Dockerfile_reference___Docker_Docs.html','w', encoding='utf-8') as f:
    f.write(str(soup))

    


