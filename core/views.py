from django.shortcuts import render, get_object_or_404
from .models import User, Tracking, Habit, Profile


# Create your views here.


def homepage(request):
    habits = Habit.objects.all()
    return render(request, 'homepage.html', {'habits': habits})


def landing(request):
    users = User.objects.all()
    profiles = Profile.objects.all() 

    current_user = User.objects.get(username = request.user.username)
    if current_user.username not in [profile.user.username for profile in profiles]:
        new_profile = Profile.objects.create(
            user=current_user,
            
        )
        new_profile.save()

    return render(request, 'landing.html', {'users': users, 'profiles': profiles})

def user_page(request, pk):
    habits = Habit.objects.all()
    profiles = Profile.objects.all()
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_page.html', {'user': user, 'habits': habits, 'profiles': profiles})