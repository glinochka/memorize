from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open('os - Miscellaneous operating system interfaces - Python 3.13.2 documentation.html','r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

def wrap_w(soup):
            
    def wrap_words_in_tag(text_node, tag_name):
        words = text_node.split()  
        wrapped_words = [f"<{tag_name}>{word}</{tag_name}>" for word in words] 
        new_text = " ".join(wrapped_words) 
        text_node.replace_with(BeautifulSoup(new_text, 'html.parser'))


    for i in soup.body.descendants:
        if type(i) == NavigableString and not i.isspace():
            wrap_words_in_tag(i, 'w')

    return str(soup)

wrap_w(soup)

with open('os - Miscellaneous operating system interfaces - Python 3.13.2 documentation.html','w', encoding='utf-8') as f:
    f.write(str(soup))



