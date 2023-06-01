from django.urls import resolve
from .models import FAQ


def number_questions(question_list):
    page_questions = {}
    key = 1

    for question in question_list:
        page_questions[str(key)] = question
        key += 1

    return page_questions


def get_questions(request):
    questions = {
        'questions': None,
        'all_questions': None
    }

    path_name = resolve(request.path_info).url_name

    if path_name == 'faq':
        question_list = FAQ.objects.all()
        questions['all_questions'] = number_questions(question_list)
    else:
        question_list = FAQ.objects.filter(is_on_homepage=True)
        questions['questions'] = number_questions(question_list)

    return questions
