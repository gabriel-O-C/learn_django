from django.urls import path

from .views import content_details, home

urlpatterns = [
    path('', home, name='index'),
	path('contents/<int:id>', content_details)
]
