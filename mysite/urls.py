from django.urls import path
from .views import PersonList, people


urlpatterns = [
    path('people/', PersonList.as_view(), name='person'),
    path('people/<str:iin>', people, name='iin'),
]
