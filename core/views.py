from django.shortcuts import render
from .models import User, Habit



# Create your views here.

def homepage(request):
    habits = Habit.objects.all()
    return render(Request, 'homepage.html', {'habits': habits})