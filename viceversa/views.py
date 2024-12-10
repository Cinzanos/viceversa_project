from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    # test_get_text = request.GET['usertext']
    # print(test_get_text) # получаем в cmd текст пользователя который находится в url после usertext= 
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text}) # создадим ключ и значение чтобы получать по ключу информацию
# с файле reverse.html