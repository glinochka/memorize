from django.shortcuts import render, redirect
from .models import Articles, Words, Many_Words
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
    if request.method == 'POST': title = request.POST.get('title')
    elif request.method == 'GET': title = request.GET.get('title')

    if request.method == 'POST':
        post = request.POST
        article = Articles.objects.get(title = title)
        if 'words' in post:
            start = int(post.get('id_start_word'))
            end = int(post.get('id_end_word'))

            many_words = Many_Words.objects.filter(article = article, id_start_word__range = (start,end)) \
                | Many_Words.objects.filter(article = article, id_end_word__range = (start,end))

            words = Words.objects.filter(article = article, id_word__range = (start,end))

            all_old_words = list(many_words) + list(words)

            if len(all_old_words):
                for i in all_old_words: i.delete()
            Many_Words(article=article, id_start_word = start, id_end_word = end, words = post.get('words'), transl = post.get('trans')).save()
        else:
            id = int(request.POST.get('id'))
            many_words = Many_Words.objects.filter(article = article, id_start_word__lte = id) \
                & Many_Words.objects.filter(article = article, id_end_word__gte = id)
            
            word = Words.objects.filter(article = article, id_word = id)
            if many_words.exists():
                for i in many_words: i.delete()

            if word.exists():
                word.update(transl = post.get('trans'))
            else:
                Words(article=article, id_word = int(post.get('id')),word = post.get('word'), transl = post.get('trans')).save()
    
    if title:
        article = Articles.objects.get(title = title)
        dir = article.article.file
        file_name = dir.name.split('/')[-1].split('\\')[-1]

        transles = [[w.id_word, w.transl] for w in list(Words.objects.filter(article = article))]
        many_transles = [[w.id_start_word, w.id_end_word, w.transl] for w in list(Many_Words.objects.filter(article = article))]
        data = {
            'title': title,
            'transles': transles,
            'many_transles': many_transles
        }

        data = json.dumps(data, cls=DjangoJSONEncoder)
        context = {'data' : data}
        return render(request, f'{request.user.username}/{file_name}', context)
    else:
        return render(request, f'somethings_wrong.html')
    
               
    

