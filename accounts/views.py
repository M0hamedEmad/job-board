from django.shortcuts import render, redirect
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth import authenticate,login
from .models import Profile
from django.contrib.auth.decorators import login_required

def SignUp(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data.get('username')
            password = form.changed_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

            return redirect('profile')

    else:
        form = SignUpForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()

    return render(request, 'registration/profile.html', {'profile':profile})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(data=request.POST ,instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid:
            user_form.save()
            profile_form.save()

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'registration/edit_profile.html', {'form1':user_form, 'form2':profile_form})