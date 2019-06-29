from django.shortcuts import render, get_object_or_404

from .models import Article


def year_archive(request, year):
    article_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': article_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    article_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month': month, 'article_list': article_list}
    return render(request, 'news/month_archive.html', context)

def article_detail(request, year, month, pk):
    article_obj = get_object_or_404(Article, pk=pk, pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month': month, 'article_obj': article_obj}
    return render(request, 'news/article_detail.html', context)
