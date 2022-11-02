from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница, привет')

# Страница со сгруппированными постами
def group_posts(request, slug):
    return HttpResponse(f'пост "{slug}" в списке сгруппированных постов или что-то в этом духе')