from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    cards_list = [1,2,3,4,5,6]
    return render(request, 'contents/pages/home.html', {'cards_list': cards_list})


def content_details(request: HttpRequest, id: int) -> HttpResponse:
    cards_list = [1,2,3,4,5,6]
    return render(request, 'contents/pages/content-details.html', {'cards_list': cards_list, 'id': id})
