from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def about(request):
    logger.info(f"Была запущена функция: {about.__name__}")
    return HttpResponse("<h2>Я Никита, мне 14 лет. Пишу программы с 12. Это мой первый Django-сайт!</h2>")