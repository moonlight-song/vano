from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Human
from .serializers import HumanSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

def index (request):
    return render(request, 'diht/index.html', None)

def displayNewsList (request):
    return HttpResponse("The news list goes here")

def displayFullArticle (request, articleUrl) :

    article = Article.objects.get (url = articleUrl)

    context = {
        'article' : {
            'title' : article.title,
            'text' : article.previewText,
            'date' : article.dateCreated.strftime ("%d.%m.%Y %H:%M")
        },
    }
    return render(request, 'diht/article.html', context)


class HumanView (viewsets.ModelViewSet) :
    queryset = Human.objects.all()
    serializer_class = HumanSerializer


class Books (APIView) :

    def get (self, request, *args, **kwargs) :
        return Response ("Hey there " + str (kwargs['book_id']))