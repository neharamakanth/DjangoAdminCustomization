from VideoApp import views
from django.urls import path

#template tagging global variable app_name

app_name='VideoApp'


urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative_urls,name='relative'),
]
