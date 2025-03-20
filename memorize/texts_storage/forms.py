from .models import Articles
from django import forms

class NewArticle(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'article')
        labels = {'article': 'Отправте страницу статьи. Обязательно в формате .HTML',
                  'title': 'Название'}
    def __init__(self, *args, **kwargs):
        super(NewArticle, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'articles':
                field.widget.attrs.update({'class': 'form-control form-label bg-dark text-white mx-auto m-2',
                                        'style': 'width: 60%'}) 
            else:
                field.widget.attrs.update({'class': 'form-control form-label bg-dark text-white mx-auto m-2',
                                        'style': 'width: 80%'})
        #self.fields['articles'].required = False

