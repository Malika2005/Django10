from django.shortcuts import render, redirect
from .models import Profile

def index(request):
    profiles = Profile.objects.all
    return render(request, 'index.html', {'profiles': profiles})

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        age = request.POST['age']
        hobbies = request.POST['hobbies']
        music = request.POST['music']
        short_info = request.POST['short_info']
        profile = Profile(name=name, age=age, hobbies=hobbies, music=music, short_info=short_info)
        profile.save()
        return redirect('index')
    return render(request, 'register.html')

def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {'profile': profile})
