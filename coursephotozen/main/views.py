from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, "main/index.html", data)