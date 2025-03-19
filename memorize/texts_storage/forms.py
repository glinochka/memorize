from .models import Texts
from django import forms

class Newtext(forms.ModelForm):
    class Meta:
        model = Texts
        fields = ('title', 'text')
        labels = {'text': 'Введите текст. Обязательно в формате .TXT',
                  'title': 'Название'}
    def __init__(self, *args, **kwargs):
        super(Newtext, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'text':
                field.widget.attrs.update({'class': 'form-control form-label bg-dark text-white mx-auto m-2',
                                        'style': 'width: 40%'}) 
            else:
                field.widget.attrs.update({'class': 'form-control form-label bg-dark text-white mx-auto m-2',
                                        'style': 'width: 80%'})
        self.fields['text'].required = False

