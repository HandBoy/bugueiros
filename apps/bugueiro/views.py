from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import UserForm, ProfileForm, SignUpForm
from .models import Profile;
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Permission

# Create your views here.


def index(request):
    context = {}
    # context['cursos'] = Curso.objects.all()
    return render(request, template_name='index.html', context=context)


@login_required
def dashboard(request):
    context = {}
    return render(request, template_name='dashboard.html', context=context)

@login_required
def user_list(request):
    context = {}
    context['usuarios'] = User.objects.all()
    return render(request, 'profile/list.html', context)

@login_required
@transaction.atomic
def update_profile(request, pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.user = user
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('settings:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user = get_object_or_404(User, pk=pk)
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'profile/add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user,
    })

@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.location = form.cleaned_data.get('location')
            #user.profile.photo = form.cleaned_data.get('photo')
            #user.profile.permission = form.cleaned_data.get('permission')
            user.profile.gender = form.cleaned_data.get('gender')
            user.save()
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'user_form': form})


@login_required
def profile(request):
    context = {}
    return render(request, template_name='profile/profile.html', context=context)