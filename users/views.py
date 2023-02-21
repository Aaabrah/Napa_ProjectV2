from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProfilesModel
from .forms import ProfileForm, UserForm


@login_required
def ProfileView(request):
    user = get_object_or_404(ProfilesModel, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=user)
    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def logout_view(request):
    logout(request)
    return redirect('main:home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
