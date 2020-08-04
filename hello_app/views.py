from django.shortcuts import render

# Create your views here.
def index(request):
    my_var = 'WORLD'
    return render(request, 'hewwo.html', {'my_var': my_var})