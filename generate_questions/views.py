from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from openai import OpenAI
from generate_questions.utils import get_article, get_questions

def generate_questions(request):

    if request.method == 'POST':  # comes here when you are making a post request via submitting the form
        # client = OpenAI()
        article_data = get_article(request.POST['article_name'])
        extract = article_data['extract'][:5000]  # don't send too many tokens
        questions = get_questions(
            request.POST['number'],
            request.POST['article_name'],
            extract,
            request.POST['level']
            )
        context = {
            "questions": questions,
        }
        template = loader.get_template('questions.html')

        return HttpResponse(template.render(context=context, request=request))
    else:
        template = loader.get_template('question.html')
        return HttpResponse(template.render(request=request))
