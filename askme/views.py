from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from askme.models import *


def paginate(objects_list, request, per_page=6):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page=per_page)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def index(request) -> HttpResponse:
    questions = Question.manager.get_some_questions()
    paged_obj = paginate(objects_list=questions, request=request)
    context = {'questions': paged_obj,
               'paged_obj': paged_obj, }
    return render(request, 'index.html', context=context)


def hot(request):
    questions = Question.manager.get_hot_questions()
    paged_obj = paginate(objects_list=questions, request=request)
    context = {'questions': paged_obj,
               'paged_obj': paged_obj, }
    return render(request, 'index.html', context=context)


def ask(request) -> HttpResponse:
    return render(request, 'ask.html')


def questions_with_tag(request, id):
    try:
        Tag.objects.get(pk=id)
        questions = Question.manager.get_question_with_tag(tag_id=id)
    except Exception:
        return HttpResponseNotFound("ERROR 404: NOT FOUND")
    questions = Question.manager.get_question_with_tag(tag_id=id)
    paged_obj = paginate(objects_list=questions, request=request)

    context = {'questions': paged_obj,
               'paged_obj': paged_obj}

    return render(request, 'index.html', context=context)


def question(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Exception:
        return HttpResponseNotFound("ERROR 404: NOT FOUND")

    question = Question.objects.get(pk=id)
    answers = question.answers.all()
    paged_obj = paginate(objects_list=answers, request=request)
    context = {'question': question,
               'answers': paged_obj,
               'paged_obj': paged_obj}
    return render(request, 'question.html', context=context)


def login(request) -> HttpResponse:
    return render(request, 'login.html')


def settings(request) -> HttpResponse:
    return render(request, 'settings.html')


def signup(request) -> HttpResponse:
    return render(request, 'signup.html')
