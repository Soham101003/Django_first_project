from django.shortcuts import render,HttpResponse
from .models import TodoItem

# Create your views here.
def home(requests):
   # return HttpResponse("Hello World !")
    return render(requests,'home.html' )

def todos(requests):
    items = TodoItem.objects.all()
    return render(requests, "todos.html", {"todos":items})