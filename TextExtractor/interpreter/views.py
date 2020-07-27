from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from .models import Upload
from .analyze import parse_through_file
from .analyze import create_data
from .models import Data
from django.core import serializers

# Create your views here.
from .forms import CreateUserForm


@login_required(login_url='/login')
def index(request):
    return render(request, 'interpreter/index.html')


@login_required(login_url='/login')
def home(request):
    graph_data = Data.objects.all()
    upload_title = Upload.objects.all().values_list('title', flat=True).order_by('id').filter(user_id__gte=8)
    title = list(upload_title)
    data = serializers.serialize("json", graph_data)
    context = {
        "json": data,
        "title": title
    }
    return render(request, 'interpreter/home.html', context)


@login_required(login_url='/login')
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            common_words = parse_through_file(request.FILES['file'])
            new_upload = form.save()
            new_upload.user = request.user
            new_upload.save()
            create_data(new_upload.pk, common_words)
            filtered_objects = Data.objects.filter(upload=new_upload.pk)
            upload_title = Upload.objects.filter(id=new_upload.pk).values_list('title', flat=True).order_by('id')
            title = list(upload_title)
            data = serializers.serialize("json", filtered_objects)
            context = {
                "json": data,
                "form": form,
                "title": title
            }
            return render(request, "interpreter/upload.html", context)
    else:
        form = UploadForm()
    return render(request, 'interpreter/upload.html', {'form': form})


@login_required(login_url='/login')
def mylist(request):
    upload_user = Upload.objects.filter(user=request.user).values_list('id', flat=True).order_by('id')
    graph_data = Data.objects.filter(upload__in=upload_user)
    upload_title = Upload.objects.filter(user=request.user).values_list('title', flat=True).order_by('id')
    title = list(upload_title)
    data = serializers.serialize("json", graph_data)
    context = {
        "json": data,
        "title": title
    }
    return render(request, 'interpreter/mylist.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/index/')
        else:
            messages.info(request, 'Username OR password incorrect')
            return render(request, 'interpreter/login.html')

    return render(request, 'interpreter/login.html')


def logoutpage(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login/')
    else:
        form = CreateUserForm()
    return render(request, 'interpreter/register.html', {'form': form})