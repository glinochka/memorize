from django.shortcuts import render, redirect
from .models import Articles, Words
from .forms import NewArticle
from .utils import savy_html
from django.core.serializers.json import DjangoJSONEncoder
import json

def new_article(request): 
    last_article = Articles.objects.filter(user = request.user).last()
    if last_article:last_article = last_article.title
    
    if request.method == 'POST':
        form = NewArticle(request.POST,request.FILES)

        if form.is_valid():
            article = request.FILES.get('article')     
            Articles(user = request.user, article = article, title = request.POST['title'] ).save()

            savy_html(str(Articles.objects.get(title = request.POST['title']).article)) 

            return redirect('add')   
    else:
        form = NewArticle()
    
    context = {'form' : form,
               'last_article': last_article
               }
    return render(request, 'new_article.html', context)

def listof_articles(request):
    del_mes = '' 
    if request.method == 'GET':
        
        title = request.GET.get('delete')
        if title:
            try: 
                Articles.objects.get(title = title).article.delete(save=True)
                Articles.objects.get(title = title).delete()
            except WindowsError:
                del_mes = 'Упс не получилось удалить статью, попробуйте позже.'
            

    titles = []
    for i in Articles.objects.filter(user = request.user):
        titles += [i.title]

    context = {'titles' : titles,
               'del_mes': del_mes
               }
    return render(request, 'list.html', context)

def read_article(request): 
    if request.method == 'GET':
        title = request.GET.get('title')
        if title:
            article = Articles.objects.get(title = title)
            dir = article.article.file
            file_name = dir.name.split('/')[-1].split('\\')[-1]
            transles = [[w.id_word, w.transl] for w in list(Words.objects.filter(article = article))]
            
            data = {
                'title': title,
                'transles': transles
            }

            data = json.dumps(data, cls=DjangoJSONEncoder)
            context = {'data' : data}
            return render(request, f'{request.user.username}/{file_name}', context)
             
        else:
            return render(request, f'somethings_wrong.html')
    elif request.method == 'POST':
        post = request.POST
        title = post.get('title')
        article = Articles.objects.get(title = title)
        word = Words.objects.filter(article = article, id_word = int(request.POST.get('id')))

        if word.exists():
            word.update(transl = post.get('trans'))
        else:
            Words(article=article, id_word = int(post.get('id')), transl = post.get('trans')).save()

        dir = article.article.file
        file_name = dir.name.split('/')[-1].split('\\')[-1]

        transles = [[w.id_word, w.transl] for w in list(Words.objects.filter(article = article))]
        data = {
            'title': title,
            'transles': transles
        }

        data = json.dumps(data, cls=DjangoJSONEncoder)
        context = {'data' : data}

        return render(request, f'{request.user.username}/{file_name}', context)
    else:
        return render(request, f'somethings_wrong.html')
    
               
    

