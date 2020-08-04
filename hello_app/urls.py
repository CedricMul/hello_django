from django.urls import path
import hello_app.views

app_urls = [
    path('', hello_app.views.index)
]