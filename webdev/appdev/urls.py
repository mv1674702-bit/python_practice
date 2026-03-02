from django.urls import path
from appdev.views import home
urlpatterns=[
    path('', home, name='home'),
]
